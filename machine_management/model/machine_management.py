from importlib.resources import _

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MachineManagement(models.Model):
    _name = "machine.management"
    _inherit = 'mail.thread'
    _rec_name = "sequence"

    sequence = fields.Char(string='Sequence', required=True, index=True, copy=False, default='New', readonly=True)
    serial_number = fields.Char("Serial Number", unique=True)
    image = fields.Binary(string="")
    company = fields.Many2one('res.company', string='Company', track_visibility='onchange',
                              readonly=True, default=lambda self: self.env.company)
    name = fields.Char(string="Machine Name")
    date_of_purchase = fields.Date("Date Of Purchase", tracking=True, help="add purchase date")
    purchase_value = fields.Integer("Purchase Value", help="add purchase value")
    customer = fields.Many2one(comodel_name='res.partner', string="Customer", help="add name of customer")
    state = fields.Selection(
        string='State',
        selection=[('active', 'Active'),
                   ('in_service', 'In Service')], default="active")
    description = fields.Char("Description", help="add description of products")
    instruction = fields.Char("Instruction")
    warranty = fields.Selection(
        string='Warranty',
        selection=[('yes', 'Yes'),
                   ('no', 'No')])
    machine_instructions = fields.Html("Machine Instructions", help="add instruction of machine")
    machine_type = fields.Selection(string='Machine Type',
                                    selection=[('vending', 'Vending'),
                                               ('cooler', 'Cooler'),
                                               ('laundry', 'Laundry')])

    _sql_constraints = [('serial_number_unique', 'unique(serial_number)', 'The serial number must be unique!')]

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('machine')
        return super(MachineManagement, self).create(vals)

    @api.constrains('purchase_value')
    def _check_purchase_value(self):
        if self.purchase_value <= 0:
            raise ValidationError("The purchase value should not be less than or equal to 0.")

    @api.constrains('serial_number')
    def _check_serial_number(self):
        for num in self:
            count = self.sudo().search_count([('serial_number', '=', num.serial_number)])
            if count > 1:
                raise ValidationError(_("The number is already exists"))



























