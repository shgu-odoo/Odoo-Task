# -- coding: utf-8 --

from odoo import models 


class ResUsers(models.Model):
    
    _inherit = 'res.users'

    # ==========================
    # Method Declaration
    # ==========================

    def name_get(self):
        result = []
        for users in self:
            name = users.name +' [ '+ users.login +' ] '
            result.append((users.id, name))
        return result