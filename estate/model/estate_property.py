from datetime import timedelta

from odoo import models, fields


class TestModel(models.Model):
    _name = "estate"

    name = fields.Char("Title")
    description = fields.Text("Description")
    postcode = fields.Char("postcode")
    date_availability = fields.Date("Available from", default=fields.Date.today() + timedelta(days=92), copy=False)
    expected_price = fields.Float("Expected price")
    selling_price = fields.Float("Selling price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default="2")
    living_area = fields.Integer("living area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("garage")
    garden = fields.Boolean("Garden")
    garden_orientation = fields.Selection(
        string='garden orientation',
        selection=[('North', 'North'),
                   ('South', 'South'),
                   ('East', 'East'),
                   ('West', 'West')])

    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer received', 'Offer Received',), ('offer accepted', 'Offer Accepted'),  ('sold', 'Sold'), ('canceled', 'Canceled')],
        required=True, copy=False, default="new")
    garden_area = fields.Integer("garden area")

