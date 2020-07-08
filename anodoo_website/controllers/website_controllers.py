# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.website.controllers.main import Website
from odoo.http import request, route
import werkzeug


from odoo.addons.website_profile.controllers.main import WebsiteProfile
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError

class AnodooProfile(WebsiteProfile):
    
    
    #增加('category', '=', 'default') 限制
    #Override
    @http.route()
    def view_ranks_badges(self, **kwargs):
        ranks = []
        if 'badge_category' not in kwargs:
            Rank = request.env['gamification.karma.rank']
            ranks = Rank.sudo().search([('category', '=', 'default')], order='karma_min DESC')

        Badge = request.env['gamification.badge']
        badges = Badge.sudo().search(self._prepare_badges_domain(**kwargs))
        badges = sorted(badges, key=lambda b: b.stat_count_distinct, reverse=True)
        values = self._prepare_user_values(searches={'badges': True})

        values.update({
            'ranks': ranks,
            'badges': badges,
            'user': request.env.user,
        })
        return request.render("website_profile.rank_badge_main", values)
    
    @http.route('/profile/ranks_list', type='http', auth="public", website=True)
    def view_ranks_list(self, **kwargs):

        Rank = request.env['gamification.karma.rank']
        ranks = Rank.sudo().search([('category', '=', 'default')], order='karma_min DESC')


        values = {
            'ranks': ranks,
        }
        
        return request.render("anodoo_website.rank_list_main", values)
    
    @http.route('/profile/badges_list', type='http', auth="public", website=True)
    def view_badges_list(self, **kwargs):

        Badge = request.env['gamification.badge']
        badges = Badge.sudo().search(self._prepare_badges_domain(**kwargs))
        badges = sorted(badges, key=lambda b: b.stat_count_distinct, reverse=True)
        values = self._prepare_user_values(searches={'badges': True})

        values.update({
            'badges': badges,
        })
        return request.render("anodoo_website.badge_list_main", values)
    
class AnodooPortal(CustomerPortal):
    
    
    @route(['/portal',
            '/portal/<string:portal>',
            ], type='http', auth="user", website=True)
    def portal_home(self, portal=None, **kw):
        current_portal = None
        if portal:
            p = request.env['anodoo.portal']
            portals = p.search([('code', '=', portal)], limit=1)
            if len(portals) > 0:
                current_portal = portals[0]
        
        if not portal or not current_portal:
            return werkzeug.utils.redirect('/my', code=302)
        
        #todo:权限判断
#         group_id = current_portal.group_id
#         if not request.env.user.has_group(group_id):
#             raise AccessError(_("Access Denied"))
        
        view = current_portal.view_id.xml_id       
        
        values = self._prepare_portal_layout_values()
        return request.render(view, values)
    
class LoginHome(Website):
    
    #重写方法，当非后台用户登录成功后，从/my改为去首页
    @http.route()
    def web_login(self, redirect=None, *args, **kw):
       
        response = super(Website, self).web_login(redirect=redirect, *args, **kw)
        if not redirect and request.params['login_success']:
            if request.env['res.users'].browse(request.uid).has_group('base.group_user'):
                redirect = b'/web?' + request.httprequest.query_string
            else:
                redirect = '/' #改/my 为 /
            return http.redirect_with_hash(redirect)
        
        return response
    
    