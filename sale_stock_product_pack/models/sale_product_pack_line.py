# Copyright 2019 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class SaleProductPackLine(models.Model):
    _name = 'sale.product.pack.line'

    sale_order_line_id = fields.Many2one(
        'sale.order.line',
        'Parent Product',
        ondelete='cascade',
        index=True,
        required=True,
    )