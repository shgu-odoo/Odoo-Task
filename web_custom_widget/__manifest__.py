{
    #  Information

    'name': 'Web Custom Widget',
    'version': '15.0.0',
    'summary': 'Web Custom Widget',
    'description': """
        Web Custom Widget """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['sale_management' , 'account'],
    'data': [
        'views/sale_order_views.xml',
       
    ], 
    
    'assets': {
         'web.assets_backend': [ 
             'web_custom_widget/static/src/legacy/js/widgets/shgu.js',
             'web_custom_widget/static/src/legacy/scss/shgu.scss',
         ],

    },

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 