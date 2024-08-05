from odoo import fields, models


class Employee(models.Model):
    _inherit = "hr.employee"
    # specialization = fields.Char(string="Specialization")
    specialization_ids = fields.Many2many('res.partner', string='Specialization')




