# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

class Users(models.Model):
    _inherit = 'res.users'
    
    
    @api.model
    def _update_last_login(self):
        
        super()._update_last_login()
        
        user_id = request.env.user.id
        login_ip = request.httprequest.remote_addr
        
        self.env['anodoo.login.record'].create({'user_id':user_id, 'login_ip':login_ip})