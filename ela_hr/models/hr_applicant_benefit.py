# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HrApplicantBenefit(models.Model):
    _name = "hr.applicant.benefit"
    _description = "Hr applicant benefit"
    _order = "id"

    name = fields.Char("Name", required=True)
