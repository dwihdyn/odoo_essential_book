from odoo import fields, models,api

class new_module(models.Model):
    _inherit ='sale.order'
    new_field = fields.Char(string='babi number')