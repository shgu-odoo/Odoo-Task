{
    #  Information

    'name': 'Employees Customization',
    'version': '15.0.0',
    'summary': 'Employees Customization',
    'description': """
        Employees Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency

    'depends': ['hr'],
    'data': [
        'data/cron.xml',
        'data/mail_template.xml',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application': True,

}
