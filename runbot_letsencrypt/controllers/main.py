# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime, timedelta
from openerp import http, fields
from openerp.http import request
from openerp.addons.runbot import runbot


class RunbotController(runbot.RunbotController):
    @http.route(
        "/runbot/build/<model('runbot.build'):build>/request_ssl_certificate",
        type='http', auth="public", website=True
    )
    def request_ssl_certificate(self, build, **kwargs):
        if not build.repo_id.nginx or not self._can_request_ssl_cert():
            return self.build(build.id, **kwargs)
        build._request_certificate()
        return self.build(build.id, **kwargs)

    def _can_request_ssl_cert(self):
        env = request.env
        if not env.user.has_group('runbot_letsencrypt.group_request_ssl_cert'):
            return False
        if self._get_cert_count() >= self._get_max_certs():
            return False
        return True

    def _get_cert_count(self):
        return request.env['runbot.build'].search_count([
            ('ssl_certificate_path', '!=', False),
            ('create_date', '>=', fields.Datetime.to_string(
                datetime.now() - timedelta(days=7)
            )),
        ])

    def _get_max_certs(self):
        return int(request.env['ir.config_parameter'].get_param(
            'runbot.max_certs_per_week', 99
        ))

    def build_info(self, build):
        result = super(RunbotController, self).build_info(build)
        result.update({
            'can_request_ssl_cert': self._can_request_ssl_cert(),
            'available_certs': self._get_max_certs() - self._get_cert_count(),
        })
        return result
