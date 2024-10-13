from odoo import models, fields



class classes(models.Model):

    _name = 'task.classes'

    name = fields.Char(string='Name')
    grade = fields.Char(string='Grade')

    noOfStudents = fields.Integer(compute="_get_noOfStudents", default=0)


    responsable = fields.Many2one('hr.employee', string='Responsable', domain="[('employee_type_for_task', '=', 'specialist')]")

    stuffOne2Many = fields.One2many('task.stuff', 'classOne2Many')


    def _get_noOfStudents(self):
        for rec in self:
            result=rec.env['task.students'].search([('studentClass','=',rec.name)])
            if result:
                rec.noOfStudents=len(result)
