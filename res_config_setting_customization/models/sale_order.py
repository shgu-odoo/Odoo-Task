# -- coding: utf-8 --

from odoo import models,fields,api


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    # ==========================
    # Field Declaration
    # ==========================

    sales_person = fields.Char(string='Sales Person', default='Shraddha')
    is_salesperson = fields.Boolean(string='Is Boolean',compute = '_compute_sales_person')
    
    # ==========================
    # Method Declaration
    # ==========================


    @api.depends('sales_person')
    def _compute_sales_person(self) :
        for record in self:
            record.is_salesperson = self.env['ir.config_parameter'].sudo().get_param('res_config_setting_customization.is_salesperson')

    
    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        config_user_id = self.env['ir.config_parameter'].sudo().get_param('res_config_setting_customization.sales_person')
        if config_user_id:
            result.user_id = config_user_id
        return result