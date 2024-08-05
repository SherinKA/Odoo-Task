from odoo import models, fields


class MachineTransfer(models.Model):
    _name = "machine.transfer"

    machine = fields.Char("Machine")
    # machine = fields.Many2one(comodel_name='machine.management', string='Machine')
    serial_number = fields.Char("Serial Number")
    transfer_date = fields.Date("Transfer Date")
    transfer_type = fields.Selection(
        string='Transfer Type',
        selection=[('install', 'Install'),
                   ('remove', 'Remove')])
    customer = fields.Many2one(comodel_name='res.partner', string="Customer")
    information = fields.Char("Information")


