# -- coding: utf-8 --

from odoo import models,fields


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    # ==========================
    # field Declaration
    # ==========================

    is_salesperson = fields.Boolean(string='Is SalesPerson', config_parameter="res_config_setting_customization.is_salesperson")
    sales_person = fields.Many2one('res.users', config_parameter="res_config_setting_customization.sales_person")