from odoo import api,models,fields

class AutoalterCustomer(models.Model):
    _name='autoalter.customer'
    _description='show customer'
    _rec_name="user_name"

    user_name=fields.Char(string="Owener name")
    user_veh_img=fields.Image(string="Vehicle Image")
    user_email=fields.Char(string="Email id")
    user_no=fields.Char(string="Contact no")

    select_cust_ids=fields.Many2many('autoalter.customizer',string="Select Customizer")

    #@api.depends("select_cust_ids.cust_avil")
    #def _compute_available(self):
        #cus_list=[]
        #for record in self.select_cust_ids:
        #        if record.cust_avil:
        #            cus_list.append(record)
        #print(cus_list)
        #self.select_cust_ids=cus_list
        #for record in self:
        #    record.select_cust_ids = any(l.cust_avil == True for l in record.select_cust_ids)