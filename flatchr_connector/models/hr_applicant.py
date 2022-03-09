# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, api, models, _
from odoo.exceptions import UserError, ValidationError
import logging
import csv
import urllib
import base64
import io

_logger = logging.getLogger(__name__)


class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    applicant_source = fields.Char(string="Applicant source")
    flatchr_applicant_id = fields.Char(string="Flatchr Applicant ID")
    job_state = fields.Selection(string="Job state", related="job_id.state", store=True)
    job_count = fields.Integer(compute='_compute_job_count', string="# Jobs")
    date_source = fields.Datetime(string='Date de synchronisation', help="Date à laquelle le candidat a été enregistré dans Odoo via l'API", tracking=True)
    #cv_link = fields.Char(string="CV link")

    @api.depends('application_count')
    def _compute_job_count(self):
        for applicant in self:
            applicant.job_count = applicant.application_count + 1

    def action_show_jobs(self):
        applicant_ids = self.env['hr.applicant'].with_context(active_test=False).search([('email_from', '=', self.email_from)])

        return {
            'type': 'ir.actions.act_window',
            'name': _('Applicant jobs'),
            'res_model': 'hr.job',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', applicant_ids.mapped('job_id').ids)]
        }

    @api.depends('email_from')
    def _compute_application_count(self):
        application_data = self.env['hr.applicant'].with_context(active_test=False).read_group([
            ('email_from', 'in', list(set(self.mapped('email_from'))))], ['email_from'], ['email_from'])
        application_data_mapped = dict((data['email_from'], data['email_from_count']) for data in application_data)
        applicants = self.filtered(lambda applicant: applicant.email_from)
        for applicant in applicants:
            applicant.application_count = application_data_mapped.get(applicant.email_from, 1) - 1

            if applicant.application_count > 0:
                _logger.info("******* New job %s" % applicant.job_id.name)

        (self - applicants).application_count = False

    def action_applications_email(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Applications'),
            'res_model': self._name,
            'view_mode': 'tree,kanban,form,pivot,graph,calendar,activity',
            'domain':  [('email_from', 'in', self.mapped('email_from'))],
            'context': {'active_test': False}
        }

    @staticmethod
    def import_cvs(env, csv_file):
        file = base64.b64decode(csv_file)
        data = io.StringIO(file.decode("utf-8"))
        data.seek(0)
        file_reader = []
        csv_reader = csv.reader(data, delimiter=';')
        file_reader.extend(csv_reader)
        
        for row in file_reader:
            #row = row[0].replace('"', "")
            #row = row.split(";")
            applicant_ids = env['hr.applicant'].search([('email_from', '=', row[1])]).filtered(lambda j: j.job_id.name == row[3])
            if applicant_ids:
                applicant_id = applicant_ids[0]
                if not applicant_id.has_cv():
                    download_url = row[2]

                    try:
                        pdf_file = urllib.request.urlopen(download_url).read()

                        env['ir.attachment'].create({
                            'name': 'cv_' + applicant_id.partner_name,
                            'res_id': applicant_id.id,
                            'res_model': applicant_id._name,
                            'datas': base64.encodebytes(pdf_file),
                            'type': 'binary',
                            #'folder_id': env.ref('flatchr_connector.cv_folder').id,
                        })

                    except Exception as e:
                        _logger.error("Impossible de télécharger le CV du candidat: %s, pour la raison suivante : %s" %(applicant_id.name, e))
        return True

    def has_cv(self):
        attachment_id = self.attachment_ids.filtered(lambda att: 'cv_' + self.partner_name in att.name)
        if attachment_id:
            return True
        return False

    @staticmethod
    def open_dl_wizard(self):
        return self.env.ref('flatchr_connector.flatchr_connector_csv_dl_wizard_action').read()[0]
