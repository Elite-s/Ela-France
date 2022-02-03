{
    "name": "Flatchr Connector",
    "summary": """
        This module provides a connector to the Flatchr API.
        It regularly fetches new job offers and candidates from Flatchr in
        order to ingest them in your Odoo database.
        """,
    "category": "",
    "version": "14.0.1.0.0",
    "author": "Odoo PS",
    "website": "http://www.odoo.com",
    "license": "OEEL-1",
    "depends": [
        'hr_recruitment',
    ],
    "data": [
        "data/ir_cron.xml",
        "views/hr_applicant.xml",
        "views/res_config_settings.xml"
    ],
}
