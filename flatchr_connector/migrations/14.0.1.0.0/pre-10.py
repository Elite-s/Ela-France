import logging
import os

from odoo import SUPERUSER_ID, api
from odoo.addons.flatchr_connector.migrations import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})

    if "ODOO_STAGE" in os.environ and os.environ["ODOO_STAGE"] == "dev":
        _logger.info("Exit migration script : dev env database !")
        return
    # hr.applicant x_studio_date_source - migrate the field from studio to the new module
    # hr.applicant x_studio_source - migrate the field from studio to the new module

    _logger.info("######################### Begin pre_10 #########################")

    _logger.info("----------RENAME MODELS----------")

    to_rename_models = ()

    for model in to_rename_models:
        _logger.info("rename model : %s -> %s" % (model[0], model[1]))

        cr.execute("UPDATE ir_model SET state='base' WHERE model LIKE %s", [model[0]])
        util.rename_model(cr, model[0], model[1], rename_table=model[2])

    _logger.info("----------RENAME FIELDS----------")

    to_rename_fields = (
        ('hr.applicant', 'x_studio_date_source', 'date_store'),
        ('hr.applicant', 'x_studio_source', 'applicant_source')
    )

    for field in to_rename_fields:
        _logger.info("rename field : %s -> %s on model %s" % (field[1], field[2], field[0]))

        cr.execute("UPDATE ir_model_fields SET state='base' WHERE name LIKE %s AND model LIKE %s", [field[1], field[0]])
        util.rename_field(cr, field[0], field[1], field[2])

    _logger.info("----------REMOVE VIEW----------")
