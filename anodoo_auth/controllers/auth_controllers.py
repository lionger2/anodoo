# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.web.controllers.main import Home
from odoo.http import request

class LoginHome(Home):
    
    @http.route(['/web/login', '/crm/login'], type='http', auth="none")
    def web_login(self, redirect=None, *args, **kw):
        
        path = request.httprequest.path;
        if path == '/crm/login':
            request.params['crm_login'] = True
        
        response = super(LoginHome, self).web_login(redirect=redirect, *args, **kw)
               
        return response
    
    