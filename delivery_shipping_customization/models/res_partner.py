# -- coding: utf-8 --

from odoo import models,fields


class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    # ==========================
    # field Declaration
    # ==========================

    days_to_deliver = fields.Integer(string = 'Days to Deliver')

