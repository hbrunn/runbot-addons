# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import ConfigParser
import logging
from openerp import api, fields, models


class Letsencrypt(models.AbstractModel):
    _inherit = 'letsencrypt'

    @api.model
    def call_cmdline(self, cmdline, loglevel=logging.INFO,
                     raise_on_result=True):
        if cmdline[:3] == ['openssl', 'req', '-new']:
            self._runbot_hook_commandline(cmdline)
        return super(Letsencrypt, self).call_cmdline(
            cmdline, loglevel=loglevel, raise_on_result=raise_on_result,
        )

    @api.model
    def _runbot_hook_commandline(self, cmdline):
        config = None
        subj = None
        for i in range(len(cmdline)):
            if cmdline[i] == '-config':
                config = cmdline[i + i]
            if cmdline[i] == '-subj':
                subj = cmdline[i + i][3:]
        if not config or not subj:
            return
        config_parser = ConfigParser.RawConfigParser()
        config_parser.read(config)
        if not config_parser.has_section('SAN'):
            config_parser.add_section('SAN')
            config_parser.set('SAN', 'subjectAltName', 'DNS:%s' % subj)
        config_parser.set(
            'SAN', 'subjectAltName',
            config_parser.get('SAN', 'subjectAltName') +
            ','.join(self.env['runbot.build'].search([
                ('state', '=', 'running'),
            ]).mapped(
                lambda x: 'DNS:%s' % x.domain,
            ))
        )
        config_parser.write(open(config))
