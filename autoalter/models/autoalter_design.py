from odoo import models,fields

class AutoalterDesign(models.Model):
    _name='autoalter.design'
    _description='show designs'
    
    design_img=fields.Image(string="Design Image")
    des_name_id=fields.Many2one('autoalter.customizer',string="Designer Name")

    des_price=fields.Float(string="Price")
    des_gmail=fields.Char(string="Gmail")
