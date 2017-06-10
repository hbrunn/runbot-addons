# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class RunbotConfigSettings(models.TransientModel):
    _inherit = 'runbot.config.settings'

    default_max_certs_per_week = fields.Integer('Certificate requests/week')

    @api.model
    def get_default_parameters(self, fields):
        result = super(RunbotConfigSettings, self).get_default_parameters(
            fields
        )
        result.update({
            'default_max_certs_per_week':
            int(self.env['ir.config_parameter'].get_param(
                'runbot.max_certs_per_week', 99
            )),
        })
        return result

    @api.multi
    def set_default_parameters(self):
        result = super(RunbotConfigSettings, self).set_default_parameters()
        self.env['ir.config_parameter'].set_param(
            'runbot.max_certs_per_week', self.default_max_certs_per_week
        )
        return result
