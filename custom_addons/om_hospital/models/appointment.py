from odoo import models, fields, api
import datetime


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection(string='Gender', related="patient.gender", readonly=True)
    appointment_date = fields.Datetime(string='Appointment Date', default=datetime.datetime.now())
