from odoo import api,models,fields
import odoo.exceptions

class AutoalterCustomer(models.Model):
    _name='autoalter.customer'
    _description='show customer'
    _rec_name="user_name"

    user_name=fields.Char(string="Owener name")
    user_veh_img=fields.Image(string="Vehicle Image")
    user_email=fields.Char(string="Email id")
    user_no=fields.Char(string="Contact no")
    user_price=fields.Char(string="Expected Price")
    user_discrip=fields.Char(string="Discription(design or modification)")

    select_cust_ids=fields.Many2many('autoalter.customizer',string="Select Customizer")

    def action_select(self):
        if self.select_cust_ids.cust_avil:
            self.select_cust_ids.cust_avil=False
        

    def action_cancle(self):
        raise odoo.exceptions.UserError("record has been canceled")