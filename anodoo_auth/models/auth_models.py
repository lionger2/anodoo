# -*- coding: utf-8 -*-

from odoo import models, fields, api

#参考res.user 的 'res.users.log' 登陆人和登陆时间使用 create_uid, create_date, 但是会被清空
class LoginRecord(models.Model):
    _name = 'anodoo.login.record'    
    _rec_name = 'user_id'
    _order = 'id desc'
    _description = '用户登陆记录'
       
    user_id = fields.Many2one('res.users', string='登陆用户')
    
    login_time = fields.Datetime('登陆时间', default=lambda self: fields.datetime.now())
    
    login_ip = fields.Char(string="登陆IP")