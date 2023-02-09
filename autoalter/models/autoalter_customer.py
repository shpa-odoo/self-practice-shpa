from odoo import models,fields

class AutoalterCustomer(models.Model):
    _name='autoalter.customer'
    _description='show customer'

    user_name=fields.Char(string="Owener name")