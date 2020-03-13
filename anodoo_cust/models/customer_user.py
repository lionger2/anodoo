from odoo import models, fields, api

class CustomerUser(models.Model):
    _name = "anodoo.customer.user"
    _inherit = ['image.mixin']
    _description = '客户下的具体用户'
    _rec_name = 'user_identity'
    
    customer_id = fields.Many2one('res.partner', string='客户', domain="[('partner_type', '=', 'customer')]")
    
    
    user_identity = fields.Char('唯一标识信息', help='用户唯一标识信息')
    
    product = fields.Char('产品')
    
    register_date = fields.Date('注册日期')
    
    
    contact_id = fields.Many2one('res.partner', string='关联联系人', domain="[('partner_type', '=', 'contact')]")
    
    comment = fields.Text(string='备注', translate=False)
    
    #for test : 图像和3中附件模式
    attachment_ids = fields.Many2many('ir.attachment', 'customer_user_attachment_rel', 'customer_user_id',
                                      'attachment_id', 'Attachments',
                                      help="")
    attachment2_ids = fields.One2many('ir.attachment', compute='_compute_attachment_ids', string="Attachments2", readonly=False)
    
    ir_attachment_id = fields.Many2one('ir.attachment', string='Related attachment', ondelete='cascade')
    
    def _compute_attachment_ids(self):
        for user in self:
            user.attachment2_ids = self.env['ir.attachment'].search([('res_id', '=', user.id), ('res_model', '=', 'anodoo.customer.user')])
    
class CustomerUserOperation(models.Model):
    _name = "anodoo.customer.user.operation"
    _description = '用户操作，汇集所有的用户操作，从而进行用户分析和洞察'  
    _rec_name = 'operation_type'
    
    user_id = fields.Many2one('anodoo.customer.user', string='用户')
    
    product = fields.Char(related='user_id.product')
    
    customer_name = fields.Char(related='user_id.customer_id.name', store=True, string='客户')
    
    
    operation_type = fields.Char('操作类习惯')
    
    operation_time = _date = fields.Datetime('操作时间')
    
    comment = fields.Text(string='备注', translate=False)
    
    
    