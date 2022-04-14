# -- coding: utf-8 --

from datetime import datetime
from odoo import models


class SaleOrder(models.Model):

    _inherit = 'sale.order'


    # ==========================
    # Method Declaration
    # ==========================

    def create_sale_order(self):
        vals = {
            'partner_id': 12,
            'date_order': datetime.now()

        }
        sale_id = self.env['sale.order'].create(vals)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', sale_id)

        # all_sale_order = self.env['sale.order'].search([])
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', all_sale_order)

        # one_so = self.env['sale.order'].browse(305)
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', one_so.name)

        # two_so = self.env['sale.order'].browse(305, 304)
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', two_so)

        # two_so_2 = self.env['sale.order'].browse([305, 304])
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', two_so_2.mapped('name'))
      
        
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.create_sale_order()
        return res
