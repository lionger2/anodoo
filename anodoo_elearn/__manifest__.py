# -*- coding: utf-8 -*-
{
    'name': "在线学习",

    'summary': """
        在线学习
    """,

    'description': """
        在线学习
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-elearn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['website_slides',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/elearn_data.xml',
        'security/elearn_security.xml',
        'security/ir.model.access.csv',
        'views/elearn_views.xml',
        'views/elearn_menu.xml',
        'views/elearn_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/elearn_demo.xml',
    ],
}