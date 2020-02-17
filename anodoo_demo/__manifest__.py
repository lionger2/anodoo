# -*- coding: utf-8 -*-
{
    'name': "Anodoo 演示",

    'summary': """
        Anodoo的所有功能演示
    """,

    'description': """
        Anodoo的所有功能演示
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_auth', 'anodoo_demo', 'anodoo_invoice', 'anodoo_pay', 'anodoo_sale',
                'anodoo_base', 'anodoo_ecomm', 'anodoo_lead', 'anodoo_portal', 'anodoo_sfa',
                'anodoo_blog', 'anodoo_elearn', 'anodoo_meeting', 'anodoo_process', 'anodoo_sms',
                'anodoo_contact', 'anodoo_email', 'anodoo_mkt', 'anodoo_prod', 'anodoo_team',
                'anodoo_content', 'anodoo_engage', 'anodoo_mktauto', 'anodoo_profile', 'anodoo_tech',
                'anodoo_crm', 'anodoo_event', 'anodoo_oppor', 'anodoo_proj', 'anodoo_website',
                'anodoo_cust', 'anodoo_forum', 'anodoo_order', 'anodoo_quote',
                ],

    # always loaded
    'data': [
        'data/demo_data.xml',
        'security/demo_security.xml',
        'security/ir.model.access.csv',
        'views/demo_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
