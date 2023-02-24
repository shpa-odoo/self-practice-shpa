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

    state=fields.Selection(selection=[('new','New'),('order','Order'),('address','Address'),('buy','Buy'),('canceled','Canceled')],
        string="State",
        required=True,
		copy=False,
		default='new',
        readonly=False,
		store=True)
    stage_id2=fields.Selection(related="state")
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
   
    cust_price=fields.Char(string="Expected Price")
    stages=fields.Selection(selection=[('send','Send'),('recieve','Recieve')],
        compute="_compute_send")
    des_total_price=fields.Float(string="Design total price",
        default=0,
        compute="_compute_design")

    
    veh_total_price=fields.Float(string="Vehicle total price",
        default=0,
        compute="_compute_vehicle")
    cust_total_price=fields.Float(string="Custom total price",
        default=0)
    total_price=fields.Float(string="Total Price",
        default=0,
        compute="_compute_total_p")


    @api.depends('select_design_ids.des_price')
    def _compute_design(self):
        x=0
        for record in self.select_design_ids:
            x=x+record.des_price
        self.des_total_price=x

    @api.depends('select_vehicle_ids.veh_price')
    def _compute_vehicle(self):
        x=0
        for record in self.select_vehicle_ids:
            x=x+record.veh_price
        self.veh_total_price=x
    @api.depends('veh_total_price','cust_total_price','des_total_price')
    def _compute_total_p(self):
        for record in self:
            record.total_price=record.veh_total_price+record.cust_total_price+record.des_total_price

    def action_buy(self):
        for record in self:
            if record.state=="canceled":
                raise odoo.exceptions.UserError('Canceled properties can not be sold')
            else:
                record.state="buy"

    def action_cancle(self):
	    for record in self:
                if record.state=="buy":
                    raise odoo.exceptions.UserError('Sold properties can not be canceled')
                else:
                    record.state="canceled"
                
    price_order_ids=fields.Many2many('autoalter.custprice',string="Expected Price")

    @api.depends('select_cust_ids')
    def _compute_send(self):
        for record in self:
            if record.select_cust_ids:
                record.stages="send"