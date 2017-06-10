# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Letsencrypt for runbot",
    "version": "8.0.1.0.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Runbot",
    "summary": "Request certificates for runbot builds",
    "depends": [
        'runbot',
        'letsencrypt',
    ],
    "data": [
        "security/res_groups.xml",
        "views/runbot_branch.xml",
        "views/runbot_config_settings.xml",
        'views/templates.xml',
    ],
}
