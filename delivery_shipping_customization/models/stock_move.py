# -- coding: utf-8 --

from odoo import models


class StockMove(models.Model):
    
    _inherit = 'stock.move'

    def _get_new_picking_values(self):
        values = super(StockMove, self)._get_new_picking_values()
        requested_date = self.sale_line_id.order_id.requested_date
        if requested_date :
            values.update({'appointment_date': requested_date})
        return values