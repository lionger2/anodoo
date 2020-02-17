# -*- coding: utf-8 -*-
{
    'name': "技术架构",

    'summary': """
        技术架构,对Odoo的技术架构相关进行扩展
    """,

    'description': """
        技术架构,对Odoo的技术架构相关进行扩展
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base'],

    # always loaded
    'data': [
        'data/tech_data.xml',
        'security/tech_security.xml',
        'security/ir.model.access.csv',
        'views/tech_views.xml',
        'views/tech_menu.xml',
        'views/tech_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/tech_demo.xml',
    ],
}