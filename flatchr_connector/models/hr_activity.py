# Copyright 2022 ELITE Advanced technologies "salim.roumili@elite-s.com"
# Copyright 2022 ELITE Advanced technologies - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class HrActivity(models.Model):
    _name = 'hr.activity'
    _description = 'HR activity'

    name = fields.Char("Activity")
    flatchr_id = fields.Integer("Flatchr ID")

    _sql_constraints = [
        ('flatchr_id_uniq', 'unique (flatchr_id)', "Activity already exists !"),
    ]
