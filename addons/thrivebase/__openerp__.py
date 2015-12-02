# -*- coding: utf-8 -*-
{
    'name': "Thrivebase",

    'summary': """
        Custom Base Module for thrive customizations on the odoo framework""",

    'description': """
        A Powered Base Module for Thrive
    """,

    'author': "Minyx360",
    'website': "http://www.minyx360.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Rights',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','web','web_planner'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'webclient_templates.xml',

      
        
        
    ],
    # Javascript Files
    'js': ['static/src/js/backend.js'],
    # CSS Files
    'css': ['static/src/css/backend.css'], 
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'qweb' : [
        "views/base.xml",
       
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    
}