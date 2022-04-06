{
    #  Information

    'name': 'Sale Search Customization',
    'version': '15.0.0',
    'summary': 'Sale Search Customization',
    'description': """
        Sale Search Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency

    'depends': ['sale_management'],
    'data': [
        'views/sale_order_views.xml',

    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application': True,

}
