# -- coding: utf-8 --

from odoo import models 


class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    # ==========================
    # Method Declaration
    # ==========================

    def name_get(self):
        result = []
        for partner in self:
            name = partner.name +' [ '+ partner.country_id.name + ' ] '
            result.append((partner.id, name))
        return result


    def _name_search(self, name, args=None,operator='like',limit=100,name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|' , '|' , ('name' , operator,name),('phone' , operator ,name),('email' , operator,name)]
            return self._search(domain + args,limit=limit,access_rights_uid = name_get_uid)