from odoo import api,models,fields
import odoo.exceptions

class AutoalterCustomer(models.Model):
    _name='autoalter.customer'
    _description='show customer'
    _rec_name="user_name"

    user_name=fields.Char(string="Owener name",required=True)
    user_image=fields.Image(string="User Image")
    user_email=fields.Char(string="Email id")
    user_no=fields.Char(string="Contact no")
    user_birth=fields.Date(string="Birthdate")
    user_gend=fields.Selection(selection=[('male','Male'),('female','Female'),('other','Other')],
        string="Gender")
    
    '''def action_select(self):
        if self.select_cust_ids.cust_avil:
            self.select_cust_ids.cust_avil=False
        

    def action_cancle(self):
        raise odoo.exceptions.UserError("record has been canceled")'''

    