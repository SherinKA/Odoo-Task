from odoo import fields, models


class HospitalOp(models.Model):
    _name = "hospital.op"
    _description = "Hospital OP"

    op_number = fields.Integer("OP Number")
    dob = fields.Date("DOB")
    doctor = fields.Many2one("hr.employee")
    patient = fields.Many2one("res.partner")
    fee = fields.Float("Fee")
    age = fields.Integer("Age", related="patient.age")
    blood_group = fields.Selection(string="Blood Group", selection=[("O+ve", "O+ve"), ("O-ve", "O-ve"), ("A+ve", "A+ve"), ("A-ve", "A-ve"), ("B+ve", "B+ve"), ("B-ve", "B-ve"), ("AB+ve", "AB+ve"), ("AB-ve", "AB-ve")],
                                   related="patient.blood_group")

