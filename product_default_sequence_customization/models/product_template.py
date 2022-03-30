# -- coding: utf-8 --

from odoo import models,_,api


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    # ==========================
    # field Declaration
    # ==========================

    @api.model
    def create(self, vals):
        result = super(ProductTemplate, self).create(vals)
        list_seq = []
        if result.categ_id.assign_sequence:
            result.default_code = self.env['ir.sequence'].next_by_code('product.category.sequence')
        elif result.categ_id.parent_id:
            self.perent_sequence_category(result.categ_id, list_seq)
            if list_seq:
                result.default_code = self.env['ir.sequence'].next_by_code('product.category.sequence')
        return result

    def perent_sequence_category(self,categ_id,list_seq):
        parent_categ_id = categ_id.parent_id
        if parent_categ_id.assign_sequence:
            list_seq.append(True)
        if not parent_categ_id:
            return list_seq
        else:
            self.perent_sequence_category(parent_categ_id,list_seq)
        return list_seq
