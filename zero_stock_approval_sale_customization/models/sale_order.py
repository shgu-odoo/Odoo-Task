# -- coding: utf-8 --

from odoo import models , fields , api
from odoo.exceptions import UserError


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    # ==========================
    # field Declaration
    # ==========================
    
    zero_stock_approval = fields.Boolean(string = 'Stock Approval')
    new_bool_approval = fields.Boolean(string = 'New Approval', compute = '_compute_user_group')


    # ==========================
    # Method Declaration
    # ==========================

    def action_confirm(self):
        for record in self :
            if record.zero_stock_approval :
                return super(SaleOrder , self).action_confirm()
            else :
                raise UserError("Please Check Approval Checkbox")


    @api.depends('zero_stock_approval')
    def _compute_user_group(self) :
        self.new_bool_approval = self.env.user.has_group('sales_team.group_sale_manager')
        
