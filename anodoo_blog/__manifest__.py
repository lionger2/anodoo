# -*- coding: utf-8 -*-
{
    'name': "博客",

    'summary': """
        博客
    """,

    'description': """
        博客
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-blog",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'website_blog'],

    # always loaded
    'data': [
        'data/blog_data.xml',
        'security/blog_security.xml',
        'security/ir.model.access.csv',
        'views/blog_views.xml',
        'views/blog_menu.xml',
        'views/blog_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/blog_demo.xml',
    ],
}