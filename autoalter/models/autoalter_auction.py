from odoo import models,fields,api
from datetime import datetime,date
import odoo.exceptions

class AutoalterAuction(models.Model):
    _name='autoalter.auction'
    _description='show auction list'
    _rec_name="owner_name"

    now_dt=fields.Datetime(string="current date/time",
                           compute='_get_current_time')
    
    com_name=fields.Char(string="Company name",required=True)
    modl_name=fields.Char(string="model name",required=True)
    last_time_date=fields.Datetime(string="last date and time",required=True)
    owner_name=fields.Char(string="Owner name",required=True)
    auct_vhl_img=fields.Binary(string="Vehicle Image",required=True)
    date_purchase=fields.Date(string="Date of Purchase",required=True)
    start_price=fields.Char(string="Starting price",required=True)

    _sql_constraints=[
		('check_auct_price','CHECK (start_price>0)','Price must be positive.')
	]

    date_time=fields.Datetime(string="Auction date and time",required=True)
    own_mail=fields.Char(string="Owner Email id")
    transmission=fields.Char(string="Transmission type",required=True)
    used_year=fields.Char(string="Used year",required=True)
    fuel_type=fields.Selection(string="Fuel Type",required=True,
        selection=[('petrol','Petrol'),('disel','Disel'),('lpg','LPG'),('cng','CNG')])
    travel_dis=fields.Char(string="Traveled Distance(km)",required=True)
    registration=fields.Date(string="Registration date",required=True)
    register_in=fields.Date(string="Registrated in",required=True)
    mfg_year=fields.Char(string="Manufacturing Year")
    eng=fields.Char(string="engine Type")
    insurance=fields.Boolean(string="Insurance(true/false)",required=True)
    ttl_owner=fields.Char(string="Total Owner")
    road_tax=fields.Selection(selection=[('paid','Paid'),('not paid','not Paid')],
        string="Road Tax")
    org_rc=fields.Selection(selection=[('available','Available'),('not available','not Available')],
        string="Original rc")
    c_p_fit=fields.Selection(selection=[('yes','Yes'),('no','No')])
    spr_key=fields.Selection(selection=[('available','Available'),('not available','not Available')],
        string="Spare Key")
    egn_quality=fields.Selection(selection=[('smooth working','Smooth Working'),('default','Default')],
        string="Engine")
    air_conditn=fields.Selection(selection=[('smooth working','Smooth Working'),('default','Default')],
        string="Air Conditioner")
    interier_ele=fields.Selection(selection=[('smooth working','Smooth Working'),('default','Default')],
        string="Interior $ Electronic")
    ssb=fields.Selection(selection=[('smooth working','Smooth Working'),('default','Default')],
        string="Steering,Suspension & break")
    tyre=fields.Selection(selection=[('new','New'),('old','Old')],
        string="Tyre")
    exterior=fields.Selection(selection=[('good','Good'),('demaged','Demaged')],
        string="Interior $ Electronic")

    add_feature_ids=fields.Many2many('autoalter.feature',string="Add features",required=True)
    @api.constrains('last_time_date','date_time','registration','register_in','date_purchase')
    def check_last_date(self):
        for record in self:
            if record.date_time < datetime.combine(fields.Date.today(), datetime.min.time()):
                raise odoo.exceptions.ValidationError("auction date must be today or greatre than today.")
            if record.last_time_date <= record.date_time:
                raise odoo.exceptions.ValidationError("last date and time must be greater than auction date and time.")
            if record.registration > fields.Date.today():
                raise odoo.exceptions.UserError("must be lesser than today")
            if record.register_in > fields.Date.today():
                raise odoo.exceptions.UserError("must be lesser than today")
            if record.date_purchase > fields.Date.today():
                raise odoo.exceptions.UserError("must be lesser than today")
                        
    def _get_current_time(self):
        for record in self:
            record.now_dt = fields.datetime.now()
    
    
    def join_auction(self):
        self.ensure_one()
        my_model_records = self.env['autoalter.auctconnect'].search([])
        field_values = [record.act_id for record in my_model_records]
        
        if self.last_time_date>self.now_dt:
            if self.date_time<self.now_dt:
                for r in field_values:
                    if r == self.id:
                        print(".............................",r)
                        action = self.env.ref('autoalter.autoalter_auctconnect_action').read()[0]
                        print(".................................................",action)
                        action['views'] = [(self.env.ref('autoalter.autoalter_auctconnect_view_form').id, 'form')]
                        print("..........................................",action)
                        action['res_id'] = self.id
                        print(".......................................",action)
                        return action
                
                else:
                        
                        result={
                            "type":"ir.actions.act_window",
                            "res_model":"autoalter.auctconnect",
                            "view_mode":'form',
                            "name":"joining auction",
                            "context": {
                                "default_act_id":self.id,
                                "default_c_name":self.com_name,
                                "default_m_name":self.modl_name,
                                "default_d_purchase":self.date_purchase,
                                "default_s_price":self.start_price,
                                "default_l_dt":self.last_time_date,
                                "defaylt_auct_i":self.auct_vhl_img,
                            },
                        }
                        return result
            else:
                raise odoo.exceptions.UserError("date of this auction is not come yet")
        else:
            raise odoo.exceptions.UserError("Auction for this vehicle is closed")
