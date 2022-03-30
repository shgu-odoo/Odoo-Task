# -- coding: utf-8 --

from odoo import models,fields


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    # ==========================
    # field Declaration
    # ==========================

    barcode_label = fields.Char(string='Barcode Label')
