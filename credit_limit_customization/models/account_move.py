# -- coding: utf-8 --

from odoo import models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'
    _descreption = 'Account Move Credit Limit'

    # ==========================
    # Method Declaration
    # ==========================

    def action_post(self):
        if self.amount_total > self.partner_id.credit_limit:
            raise UserError("Credit Limit Exceeded ! Please Contact to Admin")
        return super(AccountMove, self).action_post()
