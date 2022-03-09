# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    is_manager = fields.Boolean("Est manager")
