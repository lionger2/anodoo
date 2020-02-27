# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'
    
    is_root_display = fields.Boolean('根目录显示', default=True)
    
    @api.model
    @api.returns('self')
    def get_user_roots(self):
        #重写父方法,增加is_root_display
        return self.search([('parent_id', '=', False), ('is_root_display', '=', True) ])