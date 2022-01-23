# Copyright 2019 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pack_line_ids = fields.One2many(
        'sale.product.pack.line',
        'sale_order_line_id',
        'Pack Products',
        help='Products that are part of this pack.'
    )

    @api.multi
    def _action_launch_stock_rule(self):
        res = super()._action_launch_stock_rule()
        if res:
            for line in self:
        return res