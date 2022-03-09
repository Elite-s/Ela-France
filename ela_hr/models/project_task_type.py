# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, api, models, _


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    is_move_applicant = fields.Boolean(string='Déplacer le candidat', help='Si cochée, le candidat sera déplacé dans l\'étape précisée dans le champs "Étape de déplacement"', tracking=True)
    stage_id = fields.Many2one("hr.recruitment.stage", string='Étape de déplacement', ondelete='restrict', tracking=True)