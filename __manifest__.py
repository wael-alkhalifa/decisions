# -*- coding: utf-8 -*-
{
    'name': "decisions",

    'summary': """
        decisions""",

    'description': """
        decisions
    """,

    'author': "wael alkhalifa",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nia_profile'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
        'wizard/wizard.xml',
        'report/report.xml'
    ],
    
}
