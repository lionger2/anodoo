# -*- coding: utf-8 -*-
{
    'name': "登陆与认证",

    'summary': """
        基础模块,实现用户的登陆与认证
    """,

    'description': """
        基础模块,实现用户的登陆与认证,对Odoo的auth类的所有模块进行集中扩展
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-auth",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['auth_signup', 'auth_oauth', 'auth_password_policy', 'auth_password_policy_signup',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/auth_data.xml',
        'security/auth_security.xml',
        'security/ir.model.access.csv',
        'views/auth_views.xml',
        'views/auth_oauth_views.xml',
        'views/auth_menu.xml',
        'views/auth_templates.xml',
        'views/res_config_settings_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/auth_demo.xml',
    ],
}