# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HrApplicantSkill(models.Model):
    _name = "hr.applicant.skill"
    _description = "Hr applicant skill"
    _order = "id"

    name = fields.Char("Name", required=True)
