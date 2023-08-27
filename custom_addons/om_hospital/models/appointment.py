from odoo import models, fields, api
import datetime


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient'

    patient = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection(string='Gender', related="patient.gender", readonly=True)
    ref = fields.Char(string='Reference')
    appointment_date = fields.Datetime(string='Appointment Date', default=datetime.datetime.now())
    prescription = fields.Html(string='Prescription')
    doctor_id = fields.Many2one('res.users', string="Doctor")
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string='Priority')
    status = fields.Selection([('progress', 'In Progress'), ('done', 'Done'), ('canceled', 'Canceled')], string='Status', default='progress', required=True)

    @api.onchange('patient')
    def onchange_patient(self):
        for rec in self:
            rec.ref = rec.patient.ref

    def object_action_test(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Hii Rainbow",
                'type': 'rainbow_man',
            }
        }
