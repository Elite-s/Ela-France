# -*- coding: utf-8 -*-
# Copyright 2020 F2F
# Auteur Amine TRIFI
# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import datetime
from odoo import api, fields, models


class CsvDlWizard(models.TransientModel):
    _name = 'csv.dl.wizard'
    _description = 'CSV download wizard'

    csv_file = fields.Binary(string="Fichier CSV")

    def csv_dl_apply(self):
        self.env['hr.job'].fetch_flatchr_data()
        self.env['hr.applicant'].import_cvs(self.env, self.csv_file)
