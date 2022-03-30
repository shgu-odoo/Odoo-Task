# -- coding: utf-8 --

from odoo import models,fields


class PartnerWiseUOM(models.Model):

    _name = 'partner.wise.uom' 
    _description = 'Partner Wise UoM'  

    # ==========================
    # field Declaration
    # ==========================

    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.product', required=True)
    uom_id = fields.Many2one('uom.uom', string='UOM' , domain="[('category_id','=', uom_category_id)]")
    uom_category_id = fields.Many2one(related="product_id.uom_id.category_id")



    
   