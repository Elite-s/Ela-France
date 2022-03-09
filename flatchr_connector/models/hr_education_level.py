# Copyright 2022 ELITE Advanced technologies "salim.roumili@elite-s.com"
# Copyright 2022 ELITE Advanced technologies - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class HrEducationLevel(models.Model):
    _name = 'hr.education.level'
    _description = 'HR education level'

    name = fields.Char("Education level")
    flatchr_id = fields.Integer("Flatchr ID")

    _sql_constraints = [
        ('flatchr_id_uniq', 'unique (flatchr_id)', "Education level already exists !"),
    ]
