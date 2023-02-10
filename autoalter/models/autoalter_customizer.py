from odoo import models,fields

class AutoalterCustomizer(models.Model):
    _name='autoalter.customizer'
    _description='show customizer'

    cust_img=fields.Image(string="Customizer Image")
    cust_name=fields.Char(string="Name")
    cust_emial=fields.Char(string="Email id")
    cust_no=fields.Integer(string="Contact no")
    cust_exp=fields.Integer(string="Experience(year)")
