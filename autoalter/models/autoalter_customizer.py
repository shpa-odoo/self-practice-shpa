from odoo import models,fields

class AutoalterCustomizer(models.Model):
    _name='autoalter.customizer'
    _description='show customizer'

    cust_name=fields.Char(string="Name")