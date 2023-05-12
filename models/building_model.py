from odoo import models, fields, api


class Building(models.Model):
    _name = "building.model"
    _description = "The building model"

    name = fields.Char(required=True)
    address = fields.Char()
    floors = fields.One2many(
        comodel_name="floor.model", inverse_name="building_id", string="Floors"
    )
    num_floors = fields.Integer(
        compute="_compute_num_floors", string="Number of Floors"
    )

    @api.depends("floors")
    def _compute_num_floors(self):
        for record in self:
            record.num_floors = len(record.floors)
