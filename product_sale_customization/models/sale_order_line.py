# -- coding: utf-8 --

from odoo import models,api


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'
    
    # ==========================
    # Method Declaration
    # ==========================

    @api.onchange('product_id')
    def product_id_change(self) :
        res = super().product_id_change()
        for rec in self :
            for record in rec.order_id.partner_id.partner_wise_uom_ids:
                if rec.product_id.id == record.product_id.id:
                    rec.product_uom = record.uom_id
                    break
            return res

    
    



    
