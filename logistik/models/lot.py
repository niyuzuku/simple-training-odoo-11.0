# -*- coding: utf-8 -*-
# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp

class stock_production_lot(models.Model):
    _inherit = "stock.production.lot"

    date = fields.Date('Date')
    price = fields.Integer('Price')
    no_po = fields.Char('No PO')

