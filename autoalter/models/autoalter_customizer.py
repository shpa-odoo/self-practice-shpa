from odoo import models,fields

class AutoalterCustomizer(models.Model):
    _name='autoalter.customizer'
    _description='show customizer'
    _rec_name="cust_name"

    
    cust_name=fields.Char(string="Name")
    cust_img=fields.Image(string="Customizer Image")
    cust_emial=fields.Char(string="Email id")
    cust_no=fields.Char(string="Contact no")
    cust_exp=fields.Char(string="Experience(year)")
    cust_typ_ids=fields.Many2many('autoalter.customizer.type',string="Type")
    cust_id=fields.Many2one('autoalter.customer',string="Customer id")
    cust_avil=fields.Boolean(string="Available",
        required=True)