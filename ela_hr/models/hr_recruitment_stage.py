# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, api, models, _


class HrRecruitmentStage(models.Model):
    _inherit = "hr.recruitment.stage"

    is_create_project_task = fields.Boolean(string='Créer formation', help='Si cochée, une tâche dans projet va être créée lors ce que l\'applicant est déplacé dans cette étape', tracking=True)
    is_reset = fields.Boolean(string='Réinitialiser', help='Si cochée, les candidats dans cette étape seront réinitialisés :\n'
        '- Mis dans l\'étape ayant la séquence la plus basse\n'
        '- Le recruteur désasigné\n'
        '- Les anciens messages dans le mur invisible aux commerciaux\n'
        'ceci aprés la période précisée dans le champs "Période"', tracking=True)
    periode = fields.Integer(string='Période', tracking=True)
