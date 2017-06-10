# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class RunbotBranch(models.Model):
    _inherit = 'runbot.branch'

    auto_ssl = fields.Boolean(
        'Request SSL certificate automatically',
        help='If you check this, after every (successful) build '
        'a certificate request is run. This is still subject to the '
        'weekly rate limit configured globally',
    )
