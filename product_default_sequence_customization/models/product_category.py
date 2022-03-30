# -- coding: utf-8 --

from odoo import models,fields


class ProductCategory(models.Model):

    _inherit = 'product.category'

    # ==========================
    # field Declaration
    # ==========================

    assign_sequence = fields.Boolean(string='Assign sequence')

    