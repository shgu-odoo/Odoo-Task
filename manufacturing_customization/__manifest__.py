{
    #  Information

    'name': 'Manufacturing Customization',
    'version': '15.0.0',
    'summary': 'Manufacturing Customization',
    'description': """
        Manufacturing Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['mrp' , 'mrp_workorder'],
    'data': [
        'views/mrp_workorder_views.xml' , 
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 
