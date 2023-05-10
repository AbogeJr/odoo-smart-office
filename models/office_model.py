from odoo import models, fields


class OfficeModel(models.Model):
    _name = "office.model"
    _description = "The office space model"

    name = fields.Char(required=True)
    description = fields.Text()
    floor = fields.Char()
    desks = fields.Integer()
    chairs = fields.Integer()
    capacity = fields.Integer()
    telephones = fields.Integer()
    computers = fields.Integer()
    projector = fields.Boolean()
    whiteboard = fields.Boolean()
    television = fields.Boolean()
    coffee_machine = fields.Boolean()
    refrigerator = fields.Boolean()
    microwave = fields.Boolean()
    water_dispenser = fields.Boolean()
    air_conditioner = fields.Boolean()
    booked = fields.Boolean(default=False)
    daily_rate = fields.Float(string="Daily Rate")
    reservation_ids = fields.One2many(
        comodel_name="reservation.model",
        inverse_name="office_id",
        string="Reservations",
    )
