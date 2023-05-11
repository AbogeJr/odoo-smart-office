from odoo import models, fields, api, exceptions


# from odoo.exceptions import UserError, ValidationError
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
    cost = fields.Float(string="Cost", compute="_compute_cost_days", store=True)
    days = fields.Integer(string="Days", compute="_compute_cost_days", store=True)

    @api.depends("office_id", "start_date", "end_date")
    def _compute_cost_days(self):
        for reservation in self:
            if reservation.start_date and reservation.end_date:
                if reservation.start_date > reservation.end_date:
                    raise exceptions.ValidationError(
                        "Start date must be before end date"
                    )
                days = (reservation.end_date - reservation.start_date).days
                # days = diff.days
                reservation.days = days
                reservation.cost = reservation.office_id.daily_rate * days
