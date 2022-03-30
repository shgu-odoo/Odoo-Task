# -- coding: utf-8 --

from odoo import models,fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    # ==========================
    # field Declaration
    # ==========================

    partner_wise_uom_ids = fields.One2many('partner.wise.uom','partner_id')


    


    



    
