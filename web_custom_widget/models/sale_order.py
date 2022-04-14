# -- coding: utf-8 --

from odoo import models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    # ==========================
    # Method Declaration
    # ==========================

    def action_confirm(self) :
        res = super(SaleOrder , self).action_confirm()
        return{
            'effect' : {
                'fadeout' : 'slow',
                'message' : 'Sale Order Confirmed',
                'type' : 'rainbow_man',
            }
        }
