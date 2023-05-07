from odoo import models, fields

class OfficeModel(models.Model):
    _name = "office.model"
    _description = "The office model"

    name = fields.Char(required=True)
    floor = fields.Char()
    desks = fields.Integer()
    chairs = fields.Integer()
    capacity = fields.Integer()
    telephones = fields.Integer()
    computers = fields.Integer()
    projector = fields.Boolean()
    whiteboard = fields.Boolean()
    televisions = fields.Boolean()
    coffee_machine = fields.Boolean()
    refrigerator = fields.Boolean()
    microwave = fields.Boolean()
    water_dispenser = fields.Boolean()
    air_conditioner = fields.Boolean()
    booked = fields.Boolean(default=False)
    
