# -- coding: utf-8 --

from odoo import models


class ActionConfirmWizard(models.TransientModel):
    
    _name = 'action.confirm.wizard'
    _description = 'Action Confirm Wizard'

    # ==========================
    # Method Declaration
    # ==========================

    def action_confirm_wizard(self):
        orders = self._context.get('active_ids')
        order_ids = self.env['sale.order'].browse(orders)
        for order in order_ids:
            order.action_confirm()

    def sale_order_report(self):
        return self.env.ref('sale.action_report_saleorder').report_action(self)