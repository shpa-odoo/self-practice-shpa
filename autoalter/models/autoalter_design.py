from odoo import models,fields

class AutoalterDesign(models.Model):
    _name='autoalter.design'
    _description='show designs'
    design_img=fields.Image(string="Design Image")