# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import os
import urlparse
from openerp import api, fields, models
from openerp.addons.letsencrypt.models.letsencrypt import get_data_dir


class RunbotBuild(models.Model):
    _inherit = 'runbot.build'

    ssl_certificate_path = fields.Char()
    ssl_certificate_key_path = fields.Char()

    @api.multi
    def _request_certificate(self):
        self.ensure_one()
        if self.ssl_certificate_path or not self.repo_id.nginx:
            return
        self.env['letsencrypt'].cron()
        domain = urlparse.urlparse(
            self.env['ir.config_parameter'].get_param(
                'web.base.url', 'localhost'
            )
        ).netloc
        self.write({
            'ssl_certificate_path':
            os.path.join(get_data_dir(), '%s.crt' % domain),
            'ssl_certificate_key_path':
            os.path.join(get_data_dir(), '%s.key' % domain),
        })
        # TODO: change the nginx template to use above variables
        self.env['runbot.repo'].reload_nginx()
