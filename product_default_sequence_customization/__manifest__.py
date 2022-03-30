{
    #  Information

    'name': 'Product Default Sequence Customization',
    'version': '15.0.0',
    'summary': 'Product Default Sequence Customization',
    'description': """
        Product Default Sequence Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency

    'depends': ['purchase'],
    'data': [
        'data/sequence.xml' ,
        'views/product_category_views.xml',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application': True,

}
