from odoo import api,models,fields
import odoo.exceptions

class AutoalterOrder(models.Model):
    _name="autoalter.order"
    _description="order model"
    _rec_name="seq_name"

    seq_name = fields.Char(string='Purchase order', required=True,readonly=True, default=lambda self: ('New'))
    o_email=fields.Char(related="select_customer_id.email",string="Email id",
        readonly=False,store=True)
    o_no=fields.Char(related="select_customer_id.phone",string="Contact no",
        readonly=False,store=True)
    o_image=fields.Image(string="Image",
        readonly=False,store=True)
    user_birth=fields.Date(string="Birthdate",
        readonly=False,store=True)
    user_gend=fields.Selection(string="gender",selection=[('male','Male'),('female','Female'),('other','Other')],
                               store=True,readonly=False)

    user_veh_img=fields.Image(string="Vehicle Image")
    
    user_discrip=fields.Char(string="Discription(design or modification)")

    state=fields.Selection(selection=[('new','New'),('order','Order'),('buy','Buy'),('canceled','Canceled')],
        string="State",
        required=True,
		copy=False,
		default='new',
        readonly=False,
		store=True)
    stage_id2=fields.Selection(related="state")
    select_design_ids=fields.Many2many('autoalter.design',string="Select Design")
    select_vehicle_ids=fields.Many2many('autoalter.vehicles',string="Select vehicles")

    buy_vehicle=fields.Boolean(string="Vehicle",
                               store=True,
                               readonly=False)
    buy_design=fields.Boolean(string="Design")
    buy_custom=fields.Boolean(string="Custom")

    select_customer_id=fields.Many2one('res.partner',string="Customer",required=True)
    customizer_sel_id=fields.Many2one('autoalter.customizer',string="change avail")
    offer_ids = fields.One2many("autoalter.offer", "pof_id", string="Offer")

    
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

    _sql_constraints=[
		('check_ord_price','CHECK (veh_total_price>=0 and des_total_price>=0 and cust_total_price>=0 and total_price>=0)','Price must be positive.')
	]

    @api.ondelete(at_uninstall=False)
    def _unlink_property(self):
         for record in self:
              if record.state not in ('new','canceled'):
                  raise odoo.exceptions.AccessError("only orders with stage sold and cancle are deleted.")
              
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
            if record.total_price != 0:
                record.state="order"

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
            
    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('autoalter.order')
        return super(AutoalterOrder,self).create(vals)
    
    def action_add_offer(self):
        return {
			'type': 'ir.actions.act_window',
            'res_model': 'autoalter.wizard',
            'view_mode': 'form',
            'target': 'new',
	    	'name': 'Wizard',
    	}       
    