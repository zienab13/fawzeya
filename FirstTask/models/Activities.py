from odoo import models, fields

class activities(models.Model):

    _name = 'task.activities'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    # hello zeinab
    name = fields.Char(string='Name', tracking=1)

    state = fields.Selection([('open','Open'),('canceled','Canceled'),('draft','Draft')], string='State', default='draft', tracking=1)

    responable = fields.Many2one('hr.employee', string='Responable', domain="[('employee_type_for_task', '!=', 'worker')]", tracking=1)

    membersOne2Many = fields.One2many('task.members', 'membersOne2Many', tracking=1)


    def action_cancel(self):
        self.state = 'canceled'

    def action_open(self):
        self.state = 'open'