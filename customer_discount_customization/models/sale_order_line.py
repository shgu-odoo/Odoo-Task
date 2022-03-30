# -- coding: utf-8 --

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    # ==========================
    # field Declaration
    # ==========================

    second_discount = fields.Float(string='2nd Disc. %')

    # ==========================
    # Method Declaration
    # ==========================

    @api.depends('price_subtotal', 'second_discount', 'price_unit')
    def _compute_amount(self):
        res = super()._compute_amount()
        for line in self:
            line.price_subtotal = line.price_subtotal - ((line.second_discount * line.price_subtotal) / 100)
        return res
