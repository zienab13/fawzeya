from odoo import models, fields

class Stuff(models.Model):

    _name = 'task.stuff'

    classOne2Many = fields.Many2one('task.classes')

    teacher = fields.Many2one('hr.employee', string='Teacher', domain="[('employee_type_for_task', '=', 'teacher')]")

    course = fields.Many2one('task.courses', string='Course')
