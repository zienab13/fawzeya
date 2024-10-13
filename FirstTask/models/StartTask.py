from odoo import models, fields

class start_task(models.Model):

    _inherit = 'hr.employee'

    employee_type_is_readonly = fields.Boolean()
    employee_type_for_task = fields.Selection([('teacher', 'Teacher'), ('worker', 'Worker'), ('specialist', 'Specialist')], string='Type of Employee')