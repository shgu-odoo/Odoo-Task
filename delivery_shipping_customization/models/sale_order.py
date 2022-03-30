# -- coding: utf-8 --

from odoo import models,fields,api
import datetime


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    # ==========================
    # field Declaration
    # ==========================

    requested_date = fields.Date(string = 'Appointment Date')
    commitment_date = fields.Datetime('Delivery Date', copy=False,
                                      states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
                                      help="This is the delivery date promised to the customer. "
                                           "If set, the delivery order will be scheduled based on "
                                           "this date rather than product lead times.", compute='_compute_delivery_date_change', readonly=False)

    # ==========================
    # Method Declaration
    # ==========================

    @api.depends('requested_date')
    def _compute_delivery_date_change(self):
        for record in self:
            if record.requested_date and record.partner_id.days_to_deliver > 0:
                record.commitment_date = record.requested_date - datetime.timedelta(days=record.partner_id.days_to_deliver)


    # @api.onchange('requested_date')
    # def _onchange_commitment_date(self) :
    #     for record in self :
    #         if record.requested_date and record.partner_id.days_to_deliver > 0:
    #             record.commitment_date = record.requested_date - datetime.timedelta(days=record.partner_id.days_to_deliver)



    # def action_confirm(self) :
    #     res = super(SaleOrder , self).action_confirm()
    #     for picking in self.picking_ids :
    #         picking.appointment_date = self.requested_date
    #     return res


