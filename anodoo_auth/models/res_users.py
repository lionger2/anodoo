# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

from odoo.exceptions import except_orm, Warning, RedirectWarning,AccessDenied

class Users(models.Model):
    _inherit = 'res.users'
    
    
    @api.model
    def _update_last_login(self):
        
        super()._update_last_login()
        
        user_id = request.env.user.id
        login_ip = request.httprequest.remote_addr
        
        self.env['anodoo.login.record'].create({'user_id':user_id, 'login_ip':login_ip})
        
    
    @api.model
    def auth_oauth_dingtalk(self,provide_id,userid):
        user_ids=self.search([('oauth_provider_id','=',provide_id),('oauth_uid','=',userid)])

        if not user_ids or len(user_ids)>1:
            return AccessDenied
        return (self.env.cr.dbname, user_ids[0].login, userid)

    @api.model
    def _check_credentials(self, password):
        try:
            return super()._check_credentials(password)
        except AccessDenied:
            res = self.sudo().search([('id', '=', self.env.uid), ('oauth_uid', '=', password)])
            if not res:
                raise