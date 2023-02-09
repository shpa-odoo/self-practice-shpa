from odoo import models,fields

class AutoalterAuction(models.Model):
    _name='autoalter.auction'
    _description='show auction list'
    
    act_vhl_img=fields.Image(string="Vehicle Image")