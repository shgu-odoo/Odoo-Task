{
    #  Information

    'name': 'Sale Order Wizard',
    'version': '15.0.0',
    'summary': 'Sale Order Wizard',
    'description': """
        Sale Order Wizard """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency

    'depends': ['sale_management'],
    'data': [
        'wizards/action_confirm_wizard.xml',
        'views/sale_order_views.xml',
        'security/ir.model.access.csv',

    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application': True,

}
