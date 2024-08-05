from odoo import models, fields


class MachineType(models.Model):
    _name = "machine.type"

    name = fields.Char("Name")
