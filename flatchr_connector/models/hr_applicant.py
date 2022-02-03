from odoo import fields, models


class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    applicant_source = fields.Char(string="Applicant source")
    date_store = fields.Date(string="Date store")
    flatchr_applicant_id = fields.Char(string="Flatchr Applicant ID")
