from odoo import _, fields, models
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    flatchr_api_key = fields.Char(string="Flatchr API key", default="")
    flatchr_enterprise_slug = fields.Char(string="Flatchr slug", default="")
    flatchr_company_key = fields.Char(string="Flatchr company key", default="")
    flatchr_is_cron_active = fields.Boolean(string="Active", default=lambda self: self.env.ref('flatchr_connector.cron_get_jobs_from_flatchr').active)

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('flatchr_connector.flatchr_api_key', self.flatchr_api_key)
        self.env['ir.config_parameter'].set_param('flatchr_connector.flatchr_enterprise_slug', self.flatchr_enterprise_slug)
        self.env['ir.config_parameter'].set_param('flatchr_connector.flatchr_company_key', self.flatchr_company_key)
        self.env.ref('flatchr_connector.cron_get_jobs_from_flatchr').write({
            'active': self.flatchr_is_cron_active
        })
        return res

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        api_key = self.env['ir.config_parameter'].sudo().get_param('flatchr_connector.flatchr_api_key', "")
        slug = self.env['ir.config_parameter'].sudo().get_param('flatchr_connector.flatchr_enterprise_slug', "")
        cpny_key = self.env['ir.config_parameter'].sudo().get_param('flatchr_connector.flatchr_company_key', "")
        cron_id = self.env.ref('flatchr_connector.cron_get_jobs_from_flatchr')
        res.update(
            flatchr_api_key=api_key,
            flatchr_enterprise_slug=slug,
            flatchr_company_key=cpny_key,
            flatchr_is_cron_active=cron_id.active
        )
        return res

    def test_flatchr_api_call(self):
        self.ensure_one()
        msg = _('Odoo was succesfully able to retrieve jobs and applicants from the Flatchr servers.')
        msg_type = 'success'
        
        try:
            self.env['hr.job'].fetch_flatchr_data()
        except Exception as e:
            msg = _('It looks like something went wrong when contacting the Flatchr servers. You might want to double checks your slug, API key and company key but if the problem persists after that please contact Odoo support.')
            msg_type = 'danger'
            raise ValidationError("%s" %e)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Flatchr API Test'),
                'message': msg,
                'sticky': True,
                'type': msg_type,
            }
        }
