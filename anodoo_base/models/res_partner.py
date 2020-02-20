# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Anodoo中对res.partner的基类定义
class Parnter(models.Model):
    _inherit = 'res.partner'
    
    partner_type = fields.Char('扩展类型', default='contact', help='Anodoo按照Odoo设计，用来实现contact,customer, dealer等')
    
    #重写父类，名称还是使用本身的名称
    def _get_name(self):
        return self.name