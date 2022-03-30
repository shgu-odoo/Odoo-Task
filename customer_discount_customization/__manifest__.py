{
    #  Information

    'name': 'Customer Discount Customization',
    'version': '15.0.0',
    'summary': 'Customer Discount Customization',
    'description': """
        Customer Discount Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['sale_management' , 'account'],
    'data': [
        'views/sale_order_line_view.xml' , 
        'views/account_move_line.xml' ,
        'report/sale_report.xml' ,
        'report/report_invoice_with_payments.xml' ,

    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 
