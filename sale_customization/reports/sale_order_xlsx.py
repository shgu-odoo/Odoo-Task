# -- coding: utf-8 --

from odoo import models
from datetime import datetime

class SaleOrderXlsx(models.AbstractModel):
    _name = 'report.sale_customization.sale_order_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # print("lines",lines,data)
        date_style = workbook.add_format({'text_wrap': True, 'num_format': 'dd-mm-yyyy'})
        format1=workbook.add_format({'align' : 'vcenter', 'bold' : True})
        format2=workbook.add_format({'align' : 'vcenter'})
        sheet = workbook.add_worksheet('Sale Order')
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, lines.partner_id.name, format2)
        sheet.write(3, 2, 'Order Date',format1)
        sheet.write(3, 3, lines.date_order,date_style)
        sheet.write(4, 2, 'Product', format1)
        sheet.write(4, 3, lines.order_line[0].product_id.name, format2)