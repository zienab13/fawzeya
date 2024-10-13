from odoo import models, fields, api
from datetime import date



class students(models.Model):

    _name = 'task.students'


    name = fields.Char(string='Name')
    gender = fields.Selection([('girl','Girl'),('boy','Boy')], string='Gender')
    grade = fields.Char(string='Grade')

    birthdate = fields.Date(string='Birth Date')
    dateToday = fields.Date(string='Date', default=date.today())

    emergencyPhoneNo = fields.Char(string='Emergency Phone No')
    relatives = fields.Many2many('hr.employee', string='Relatives')
    hasRelatives = fields.Boolean(string='Has Relatives', default=False)

    studentClass = fields.Many2one('task.classes', string='Student Class')
    studentActivity = fields.Many2one('task.activities', string='Student Activity')


    @api.model
    def create(self, vals):
        result = super(students, self).create(vals)

        # self.env['task.insurance'].create({
        #     'student': result.id,
        #     'dateFrom': result.dateToday
        # })
        return result

    @api.onchange('relatives')
    def relatives_onchange(self):
        if self.relatives:
            self.hasRelatives = True
        else:
            self.hasRelatives = False

    def create_insurance(self):
        return {
        'name': ('Add Insurance'),
        'type': 'ir.actions.act_window',
        'res_model': 'insurance.wizard',
        'view_mode': 'form',
        'target': 'new',
            'context':{
                'student_id': self.id
            }
    }
