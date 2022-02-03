from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    flatchr_applicant_id = fields.Char(string="Flatchr Applicant ID")
