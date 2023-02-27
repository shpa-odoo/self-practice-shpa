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
    cust_exp=fields.Char(string="Experience(year)",
        required=True)
    cust_typ_ids=fields.Many2many('autoalter.customizer.type',string="Type",
        required=True)
    status=fields.Selection(selection=[('recieve','Recieve'),('accepted','Accepted'),('rejected','Rejected')],
        store=True,
        compute="_compute_recieve")
    cust_avil=fields.Boolean(string="Available")
    order_ids=fields.Many2many('autoalter.order',string="Order id")
    price_cust_ids=fields.Many2many('autoalter.custprice',string="Expected price")
    def action_select(self):
        for record in self:
            record.cust_avil=False
            record.status="accepted"
        

    def action_cancle(self):
        for record in self:
            record.status="rejected"
            raise odoo.exceptions.UserError("record has been canceled")
    @api.depends('order_ids')
    def _compute_recieve(self):
        for record in self:
            if self.order_ids:
                record.status="recieve"
