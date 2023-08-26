from odoo import models, fields, api
import datetime


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    birth_day = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute="_compute_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    ref = fields.Char(string="Reference")
    active = fields.Boolean(string="Active", default=True)

    @api.depends('birth_day')
    def _compute_age(self):
        for record in self:
            today = datetime.date.today()
            if record.birth_day:
                record.age = today.year - record.birth_day.year
            else:
                record.age = 0

            # print(today.year)
