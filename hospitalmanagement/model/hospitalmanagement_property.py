from odoo import fields, models


class Contact(models.Model):
    _inherit = "res.partner"
    sequence_number = fields.Integer(string="Sequence Number")
    blood_group = fields.Selection(string="Blood Group",
                                   selection=[("o+ve", "o+ve"), ("o-ve", "o-ve"), ("A+ve", "A+ve"), ("A-ve", "A-ve"), ("B+ve", "B+ve"), ("B-ve", "B-ve"), ("AB+ve", "AB+ve"), ("AB-ve", "AB-ve")])
    gender = fields.Selection(string="Gender", selection=[('Male', 'Male'), ('Female','Female'), ('Others', 'Others')])
    dob = fields.Date(string="DOB")
    age = fields.Integer(string="Age")


