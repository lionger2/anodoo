# -*- coding: utf-8 -*-
{
    'name': "官网",

    'summary': """
        官网
    """,

    'description': """
        官网
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-website",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['website', 'im_livechat', 'website_livechat', 'link_tracker',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/website_data.xml',
        'security/website_security.xml',
        'security/ir.model.access.csv',
        'views/website_views.xml',
        'views/website_menu.xml',
        'views/website_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/website_demo.xml',
    ],
}