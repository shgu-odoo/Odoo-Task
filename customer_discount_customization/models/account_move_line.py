# -- coding: utf-8 --

from odoo import models,fields


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    # ==========================
    # field Declaration
    # ==========================

    second_discount = fields.Float(string = '2nd Disc. %')
