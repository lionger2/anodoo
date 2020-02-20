# -*- coding: utf-8 -*-
{
    'name': "邮件",

    'summary': """
        邮件交互
    """,

    'description': """
        邮件交互,包括邮件营销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-email",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_engage', 'anodoo_mktauto'],

    # always loaded
    'data': [
        'data/email_data.xml',
        'security/email_security.xml',
        'security/ir.model.access.csv',
        'views/email_views.xml',
        'views/email_menu.xml',
        'views/email_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/email_demo.xml',
    ],
}