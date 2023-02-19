# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Shifts(models.Model):
    _name = 'mrp.shifts'
    _description = 'Production Shifts'

    name = fields.Char(string="Name")
    from_time = fields.Float(string='From')
    to_time = fields.Float(string='To')