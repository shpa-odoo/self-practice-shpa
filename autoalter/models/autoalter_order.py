from odoo import api,models,fields
import odoo.exceptions

class AutoalterOrder(models.Model):
    _name="autoalter.order"
    _discription="order model"
    _rec_name="o_image"

    
    o_email=fields.Char(string="Email id",
        compute="_compute_oemail",readonly=False,store=True)
    o_no=fields.Char(string="Contact no",
        compute="_compute_ono",readonly=False,store=True)
    o_image=fields.Image(string="Image",
        compute="_compute_oimage",readonly=False,store=True)
    user_veh_img=fields.Image(string="Vehicle Image")
    user_price=fields.Char(string="Expected Price")
    user_discrip=fields.Char(string="Discription(design or modification)")

    select_cust_ids=fields.Many2many('autoalter.customizer',string="Select Customizer")
    select_design_ids=fields.Many2many('autoalter.design',string="Select Design")
    select_vehicle_ids=fields.Many2many('autoalter.vehicles',string="Select vehicles")

    buy_vehicle=fields.Boolean(string="Vehicle")
    buy_design=fields.Boolean(string="Design")
    buy_custom=fields.Boolean(string="Custom")

    select_customer_id=fields.Many2one('autoalter.customer',string="Customer")
    customizer_sel_id=fields.Many2one('autoalter.customizer',string="change avail")
    @api.depends("select_customer_id.user_email")
    def _compute_oemail(self):
        for record in self:
            record.o_email=self.select_customer_id.user_email
    @api.depends("select_customer_id.user_no")
    def _compute_ono(self):
        for record in self:
            record.o_no=self.select_customer_id.user_no
    @api.depends("select_customer_id.user_image")
    def _compute_oimage(self):
        for record in self:
            record.o_image=self.select_customer_id.user_image

    def action_select(self):
        for record in self:
            
                record.customizer_sel_id.cust_avil=False

    def action_cancle(self):
        raise odoo.exceptions.UserError("record has been canceled")