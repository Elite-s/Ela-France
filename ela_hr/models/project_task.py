# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, api, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    applicant_id = fields.Many2one("hr.applicant", string='Applicant')
    
    # Formation
    #formation = fields.Selection(related="applicant_id.formation", compute="_compute_formation", inverse="_set_formation")
    certification = fields.Selection(related="applicant_id.certification", string='Certification', readonly=False)
    dispositif = fields.Selection(related="applicant_id.dispositif", string='Dispositif', readonly=False)
    accompagnement = fields.Boolean(related="applicant_id.accompagnement", string='Accompagnement', readonly=False)
    connaissance = fields.Boolean(related="applicant_id.connaissance", string='Connaissance', readonly=False)
    niveau = fields.Selection(related="applicant_id.niveau", string='Niveau', readonly=False)
    nombre_dheures = fields.Integer(related="applicant_id.nombre_dheures", string='Nombre d\'heures', readonly=False)
    date_entree_call = fields.Date(related="applicant_id.date_entree_call", string='Date entrée call', readonly=False)
    date_inscription = fields.Date(related="applicant_id.date_inscription", string='Date d\'inscription', readonly=False)
    # Pédagogique
    login = fields.Char(related="applicant_id.login", string='Login', readonly=False)
    mot_de_passe = fields.Char(related="applicant_id.mot_de_passe", string='Mot de passe', readonly=False)
    date_entree = fields.Date(related="applicant_id.date_entree", string='Date d\'entrée', readonly=False)
    workhour_available_ids = fields.Many2many(related="applicant_id.workhour_available_ids", string='Horaire disponible', readonly=False)
    plateforme = fields.Selection(related="applicant_id.plateforme", string='Plateforme', readonly=False)
    motivation_appreciation = fields.Selection(related="applicant_id.motivation_appreciation", string='Motivation / Appréciation', readonly=False)
    date_fin = fields.Date(related="applicant_id.date_fin", string='Date de fin', readonly=False)
    test_result = fields.Char(related="applicant_id.test_result", string='Résultat test', readonly=False)
    ligne_suivi_ids = fields.One2many(related="applicant_id.ligne_suivi_ids", string='Tabeau de suivi', readonly=False)

    @api.onchange("stage_id")
    def _onchange_stage_id(self):
        for record in self:
            if record.stage_id.is_move_applicant_hr:
                record.applicant_id.stage_id = 8
                