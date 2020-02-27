# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    is_display_footer = fields.Boolean('博客是否显示网站Footer', config_parameter='anodoo_blog.is_display_footer')
    
    #str_date = self.env['ir.config_parameter'].sudo().get_param('crm.pls_start_date')
   
    
    
            