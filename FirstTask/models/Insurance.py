from odoo import models, fields, api

class insurance(models.Model):

    _name = 'task.insurance'

    student = fields.Many2one('task.students', string='Student')
    dateFrom = fields.Date('From Date')
    dateTo = fields.Date('To Date')
    grade = fields.Char('Grade', related='student.grade')
    name = fields.Char()


    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('task.insurance')
        rec = super(insurance,self).create(vals)
        return rec