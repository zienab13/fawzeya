from odoo import models, fields

class Members(models.Model):

    _name = 'task.members'

    membersOne2Many = fields.Many2one('task.activities')

    student = fields.Many2one('task.students', string='Student')

    grade = fields.Char(string='Grade')
