from odoo import models, fields, api


class FloorModel(models.Model):
    _name = "floor.model"
    _description = "The floor model"

    name = fields.Char(required=True)
    level = fields.Integer()
    building_id = fields.Many2one(
        comodel_name="building.model", string="Building", required=True
    )
    office_ids = fields.One2many(
        comodel_name="office.model", inverse_name="floor_id", string="Offices"
    )

    from odoo import models, fields, api


class Floor(models.Model):
    _name = "floor.model"
    _description = "The floor model"

    name = fields.Char(required=True)
    building_id = fields.Many2one("building.model", string="Building")
    office_ids = fields.One2many(
        comodel_name="office.model", inverse_name="floor_id", string="Offices"
    )
    num_offices = fields.Integer(
        string="Number of Offices", compute="_compute_num_offices", store=True
    )

    @api.depends("office_ids")
    def _compute_num_offices(self):
        for record in self:
            record.num_offices = len(record.office_ids)
