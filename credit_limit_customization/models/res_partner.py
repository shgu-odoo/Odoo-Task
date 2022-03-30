# -- coding: utf-8 --

from odoo import models,fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    # ==========================
    # field Declaration
    # ==========================

    credit_limit = fields.Float(string = 'Credit Limit')