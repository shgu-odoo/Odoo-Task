{
    #  Information

    'name': 'Product Barcode Customization',
    'version': '15.0.0',
    'summary': 'Product Barcode Customization',
    'description': """
        Product Barcode Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency

    'depends': ['stock'],
    'data': [
        'reports/product_template.xml',
        'reports/report.xml',
        'views/product_template_views.xml',

    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application': True,

}
