{
    #  Information

    'name': 'Credit Limit Customization',
    'version': '15.0.0',
    'summary': 'Credit Limit Customization',
    'description': """
        Credit Limit Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['contacts', 'sale_management'],
    'data': [
        'views/res_partner_views.xml',

    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application': True,

} 
