# -*- coding: utf-8 -*-
{
    'name': "营销自动化",

    'summary': """
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo_mktauto",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base'],

    # always loaded
    'data': [
        'data/mktauto_data.xml',
        'security/mktauto_security.xml',
        'security/ir.model.access.csv',
        'views/mktauto_views.xml',
        'views/mktauto_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}