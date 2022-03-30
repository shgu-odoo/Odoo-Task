# -- coding: utf-8 --

from odoo import models
from datetime import datetime


class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    # ==========================
    # Method Declaration
    # ==========================

    def send_birthday_wish(self):
        today_date = datetime.today().date()
        for employee in self.env['hr.employee'].search([]):
            if employee.birthday and today_date.day == employee.birthday.day and today_date.month == employee.birthday.month:
                template_id = self.env.ref('employee_customization.employee_birthday_wishes_template')
                template_id.send_mail(employee.id, force_send=True)
