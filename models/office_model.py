from odoo import models, fields, api


class OfficeModel(models.Model):
    _name = "office.model"
    _description = "The office space model"

    name = fields.Char(required=True)
    description = fields.Text()
    floor_id = fields.Many2one(comodel_name="floor.model", string="Floor")
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
    status = fields.Selection(
        selection=[("vacant", "Vacant"), ("occupied", "Occupied")], default="vacant"
    )
    daily_rate = fields.Float(string="Daily Rate")
    reservation_ids = fields.One2many(
        comodel_name="reservation.model",
        inverse_name="office_id",
        string="Reservations",
    )
    num_reservations = fields.Integer(
        string="Number of Reservations", compute="_compute_num_reservations", store=True
    )

    @api.depends("reservation_ids")
    def _compute_num_reservations(self):
        for record in self:
            record.num_reservations = len(record.reservation_ids)
