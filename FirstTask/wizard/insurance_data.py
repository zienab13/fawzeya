from odoo import models, fields

class InsuranceWizard(models.TransientModel):

    _name = 'insurance.wizard'

    dateFrom = fields.Date('From Date')
    dateTo = fields.Date('To Date')

    def create_insurance(self):
        object = self.env['task.insurance'].create({
            'student': self.env.context['student_id'],
            'dateFrom': self.dateFrom,
            'dateTo': self.dateFrom
        })
        return object