# Copyright 2010 - 2014 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# Copyright 2017 Vauxoo <info@vauxoo.com> (<https://www.vauxoo.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class RunbotBranch(models.Model):
    _inherit = "runbot.branch"

    # pylint: disable=method-compute
    branch_url = fields.Char(compute='_get_branch_url')

    @api.multi
    def _get_branch_url(self):
        for branch in self:
            if not branch.repo_id.uses_gitlab:
                super(RunbotBranch, self)._get_branch_url()
            else:
                if branch.branch_name.isdigit():
                    branch.branch_url = "https://%s/merge_requests/%s" % (
                        branch.repo_id.base, branch.branch_name)
                else:
                    branch.branch_url = ("https://%s/tree/%s" % (
                        branch.repo_id.base, branch.branch_name))
