from odoo import models,fields

class AutoalterOrder(models.Model):
    _name="autoalter.order"
    _discription="order model"

    o_name=fields.Char(string="Name")
    
