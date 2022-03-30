{
    #  Information

    'name': 'Project Customization',
    'version': '15.0.0',
    'summary': 'Project Customization',
    'description': """
        Project Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['project'],
    'data': [
        'views/project_task_views.xml' , 

    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 
