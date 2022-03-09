# Copyright 2022 ELITE Advanced technologies.
# Copyright 2022 ELITE - Salim ROUMILI
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Ela hr",
    "summary": """
        This module provides extension of hr functionalities.
        """,
    'category': 'Human Resources/Employees',
    'sequence': 199,
    "summary": "Extend employee information",
    "version": "14.0.0.0.0",
    "author": "ELITE Advanced technologies",
    "depends": ["hr", "hr_recruitment", "hr_recruitment_survey", "project"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_applicant_view.xml",
        "views/project_task_view.xml",
        "views/hr_tags_view.xml",
        "views/hr_recruitment_stage_view.xml",
        "views/project_task_type_view.xml",
        "security/security.xml",
        "data/ir_cron.xml",
    ],
    "demo": [],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
