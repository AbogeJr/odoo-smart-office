from odoo import models, fields, api


class ReservationModel(models.Model):
    _name = "reservation.model"
    _description = "The reservation model"

    name = fields.Char(required=True)
    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    office_id = fields.Many2one(
        comodel_name="office.model", string="Office", required=True
    )
    approved = fields.Boolean(default=False)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    cost = fields.Float(string="Cost", compute="_compute_cost", store=True)
    days = fields.Integer(string="Days", compute="_compute_cost", store=True)

    @api.depends("office_id", "start_date", "end_date")
    def _compute_cost(self):
        for reservation in self:
            days = (reservation.end_date - reservation.start_date).days
            reservation.days = days
            reservation.cost = reservation.office_id.daily_rate * days
