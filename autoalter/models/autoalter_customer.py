from odoo import models,fields

class AutoalterCustomer(models.Model):
    _name='autoalter.customer'
    _description='show customer'

    user_name=fields.Char(string="Owener name")
    user_veh_img=fields.Image(string="Vehicle Image")
    user_email=fields.Char(string="Email id")
    user_no=fields.Integer(string="Contact no")