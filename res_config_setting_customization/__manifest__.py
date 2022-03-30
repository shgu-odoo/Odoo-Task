{
    #  Information

    'name': 'Res Config Setting Customization',
    'version': '15.0.0',
    'summary': 'Res Config Setting Customization',
    'description': """
        Res Config Setting Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency

    'depends': ['sale_management'],
    'data': [
        'views/sale_order_views.xml',
        'views/res_config_settings_views.xml',

    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application': True,

}
