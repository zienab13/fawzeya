from email.policy import default

from odoo import models, fields, api

from Source.odoo16.odoo.tools.populate import compute


class overtime(models.Model):

    _name = 'overtime.obj'

    isUserHRManager = fields.Boolean()
    isUserEmployeeManager = fields.Boolean()
    currentUser = fields.Many2one('res.users', default=lambda self: self.env.user)
    employee = fields.Many2one('hr.employee', 'Employee',
                               compute='_compute_default_employee')
    day = fields.Date()
    hours = fields.Float()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('managerApproved', 'Manager Approved'),
        ('hrApproved', 'HR Approved')
    ], string='state', default='draft')
    notes = fields.Char()

    @api.depends('currentUser','day','hours','state','isUserHRManager')
    def _compute_default_employee(self):
        for rec in self:
            rec.employee = rec.env['hr.employee'].search([('user_id','=',rec.currentUser.id)],
                                                         limit=False)
            rec.isUserHRManager = (rec.employee.job_id.name == 'Human Resources Manager')
            if (rec.env['hr.employee'].search([('parent_id','=',rec.employee.id)])):
                rec.isUserEmployeeManager = True
                print(rec.isUserEmployeeManager)

    def action_submitted(self):
        for rec in self:
            rec.state = 'submitted'

    def action_managerApproved(self):
        for rec in self:
            rec.state = 'managerApproved'

    def action_hrApproved(self):
        for rec in self:
            rec.state = 'hrApproved'