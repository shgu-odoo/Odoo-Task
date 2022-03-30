# -- coding: utf-8 --

from odoo import models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    # ==========================
    # Method Declaration
    # ==========================
    
    def action_confirm_draft(self):
        sale_ids = self.env['sale.order'].search([('state', '=', 'draft')], limit=100)
        for order in sale_ids:
            order.action_confirm()
