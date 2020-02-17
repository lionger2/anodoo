# -*- coding: utf-8 -*-
{
    'name': "社区会员",

    'summary': """
        社区会员
    """,

    'description': """
        社区会员
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-profile",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'website_profile'],

    # always loaded
    'data': [
        'data/profile_data.xml',
        'security/profile_security.xml',
        'security/ir.model.access.csv',
        'views/profile_views.xml',
        'views/profile_menu.xml',
        'views/profile_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/profile_demo.xml',
    ],
}