from odoo import models, fields

class courses(models.Model):

    _name = 'task.courses'

    name = fields.Char(string='Name')

    teachers = fields.Many2many('hr.employee', string='Teachers', domain="[('employee_type_for_task', '=', 'teacher')]")

    headOfCourse = fields.Many2one('hr.employee', string='Head Of Course', domain="[('employee_type_for_task', '=', 'specialist')]")