# -- coding: utf-8 --

from odoo import models,fields,api
import datetime


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    # ==========================
    # field Declaration
    # ==========================

    appointment_date = fields.Date(string = 'Appointment Date')
    scheduled_date = fields.Datetime('Scheduled Date', copy=False, compute = '_compute_scheduled_date' , readonly=False)


    # ==========================
    # Method Declaration
    # ==========================

    # @api.onchange('appointment_date')
    # def _onchange_scheduled_date(self) :
    #     for record in self :
    #         if record.appointment_date and record.partner_id.days_to_deliver > 0:
    #             record.scheduled_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_to_deliver)
    

    @api.depends('appointment_date')
    def _compute_scheduled_date(self):
        for record in self:
            if record.appointment_date and record.partner_id.days_to_deliver > 0:
                record.scheduled_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_to_deliver)


    