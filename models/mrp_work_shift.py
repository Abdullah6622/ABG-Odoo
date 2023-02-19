# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MrpWorkShift(models.Model):
    _name = 'mrp.work.shift'
    _description = 'mrp work shift'

    shift_id = fields.Many2one('mrp.shifts')
    quantity = fields.Float(string='Quantity', digits='Product Unit of Measure')
    uom = fields.Many2one('uom.uom', readonly=True, related='shift_tab_id.product_uom_id')
    shift_tab_id = fields.Many2one('mrp.production')


class InheritMrpProduction(models.Model):
    _inherit = 'mrp.production'

    shifts_ids = fields.One2many('mrp.work.shift', 'shift_tab_id')

    @api.onchange('shifts_ids')
    def compute_quantity(self):
        for rec in self:
            total = 0
            for qty in rec.shifts_ids:
                total += qty.quantity

            rec.qty_producing = total
