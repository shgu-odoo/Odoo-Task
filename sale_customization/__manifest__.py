{
    #  Information

    'name': 'Sale Order Customization',
    'version': '15.0.0',
    'summary': 'Sale Order Customization',
    'description': """
        Sale Order Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['sale_management'],
    'data': [
        'data/cron.xml' ,
        'data/mail_template.xml' ,
        'reports/report.xml' ,
        'reports/report_template.xml' ,
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 