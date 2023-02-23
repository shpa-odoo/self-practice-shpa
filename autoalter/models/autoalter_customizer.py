from odoo import api,models,fields
import odoo.exceptions

class AutoalterCustomizer(models.Model):
    _name='autoalter.customizer'
    _description='show customizer'
    _rec_name="cust_name"

    
    cust_name=fields.Char(string="Name",
        required=True)
    cust_img=fields.Image(string="Customizer Image")
    cust_emial=fields.Char(string="Email id",
        required=True)
    cust_no=fields.Char(string="Contact no")
    cust_exp=fields.Char(string="Experience(year)")
    cust_typ_ids=fields.Many2many('autoalter.customizer.type',string="Type",
        required=True)
    
    cust_avil=fields.Boolean(string="Available")
    order_ids=fields.Many2many('autoalter.order',string="Order id")
    
    def action_select(self):
        for record in self:
            record.cust_avil=False
        

    def action_cancle(self):
        raise odoo.exceptions.UserError("record has been canceled")
    