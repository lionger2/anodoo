# -*- coding: utf-8 -*-
{
    'name': "anodoo_sfa",

    'summary': """
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'crm', 'sale', 'sales_team', 'sale_management', 'delivery', 'account', 'product_margin'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sfa_menu.xml',
        'views/sfa_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}