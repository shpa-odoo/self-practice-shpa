from odoo import api,models,fields
import odoo.exceptions

class AutoalterOrder(models.Model):
    _name="autoalter.order"
    _description="order model"
    _rec_name="o_no"

    
    o_email=fields.Char(string="Email id",
        compute="_compute_oemail",readonly=False,store=True)
    o_no=fields.Char(string="Contact no",
        compute="_compute_ono",readonly=False,store=True)
    o_image=fields.Image(string="Image",
        readonly=False,store=True)
    user_birth=fields.Date(string="Birthdate",
        readonly=False,store=True)
    user_gend=fields.Selection(selection=[('male','Male'),('female','Female'),('other','Other')],
        string="Gender")

    user_veh_img=fields.Image(string="Vehicle Image")
    
    user_discrip=fields.Char(string="Discription(design or modification)")

    select_cust_ids=fields.Many2many('autoalter.customizer',string="Select Customizer")
    select_design_ids=fields.Many2many('autoalter.design',string="Select Design")
    select_vehicle_ids=fields.Many2many('autoalter.vehicles',string="Select vehicles")

    buy_vehicle=fields.Boolean(string="Vehicle")
    buy_design=fields.Boolean(string="Design")
    buy_custom=fields.Boolean(string="Custom")

    select_customer_id=fields.Many2one('res.partner',string="Customer")
    customizer_sel_id=fields.Many2one('autoalter.customizer',string="change avail")
    @api.depends("select_customer_id.email")
    def _compute_oemail(self):
        for record in self:
            record.o_email=self.select_customer_id.email
    @api.depends("select_customer_id.phone")
    def _compute_ono(self):
        for record in self:
            record.o_no=self.select_customer_id.phone
    '''@api.depends("select_customer_id.user_image")
    def _compute_oimage(self):
        for record in self:
            record.o_image=self.select_customer_id.user_image'''

    '''def action_select(self):
        for record in self:
            record.select_cust_ids.cust_avil=False
                
            

    def action_cancle(self):
        raise odoo.exceptions.UserError("record has been canceled")'''

    cust_price=fields.Char(string="Expected Price")
    total_price=fields.Float(string="Total Price")