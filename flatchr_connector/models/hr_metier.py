# Copyright 2022 ELITE Advanced technologies "salim.roumili@elite-s.com"
# Copyright 2022 ELITE Advanced technologies - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class HrMetier(models.Model):
    _name = 'hr.metier'
    _description = 'HR metier'

    name = fields.Char("Metier")
    flatchr_id = fields.Integer("Flatchr ID")

    _sql_constraints = [
        ('flatchr_id_uniq', 'unique (flatchr_id)', "Metier already exists !"),
    ]
