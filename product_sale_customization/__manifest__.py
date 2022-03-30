{
    #  Information

    'name': 'Partner Wise Product Customization',
    'version': '15.0.0',
    'summary': 'Partner Wise Product Customization',
    'description': """
        Partner Wise Product Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['contacts' , 'sale_management'],
    'data': [
        'views/res_partner_views.xml' , 
        'security/ir.model.access.csv' ,
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 