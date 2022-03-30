{
    #  Information

    'name': 'Delivery Shipping Customization',
    'version': '15.0.0',
    'summary': 'Delivery Shipping Customization',
    'description': """
        Delivery Shipping Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['contacts' , 'sale_management' , 'account_accountant' , 'stock'],
    'data': [
        'views/res_partner_views.xml',
        'views/sale_order_views.xml' ,
        'views/stock_picking_views.xml' ,
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 