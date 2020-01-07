# -*- coding: utf-8 -*-
{
    'name': "Anodoo 基础",

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
    'depends': ['base', 'mail', 'mail', 'calendar', 'contacts', 'crm','sale','mass_mailing','mass_mailing_sms','website','website_slides','utm','event','survey','im_livechat','purchase','stock','account','project','hr_timesheet','hr','hr_recruitment','hr_attendance','hr_holidays','hr_expense'],

    # always loaded
    'data': [
        'data/base_data.xml',
        # 'security/ir.model.access.csv',        
        'security/base_security.xml',
        'views/base_menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}