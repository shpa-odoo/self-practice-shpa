from odoo import models,fields

class AutoalterAuction(models.Model):
    _name='autoalter.auction'
    _description='show auction list'
    _rec_name="owner_name"
    
    owner_name=fields.Char(string="Owner name")
    auct_vhl_img=fields.Binary(string="Vehicle Image")
    date_purchase=fields.Date(string="Date of Purchase")
    start_price=fields.Char(string="Starting price")
    date_time=fields.Datetime(string="Auction date and time")
    own_mail=fields.Char(string="Owner Email id")
    transmission=fields.Char(string="Transmission type")
    used_year=fields.Char(string="Used year")
    fuel_type=fields.Selection(string="Fuel Type",
        selection=[('petrol','Petrol'),('disel','Disel'),('lpg','LPG'),('cng','CNG')])
    travel_dis=fields.Char(string="Traveled Distance(km)")
    #features=fields.Text(string="Features")

    registration=fields.Date(string="Registration date")
    register_in=fields.Date(string="Registrated in")
    mfg_year=fields.Char(string="Manufacturing Year")
    eng=fields.Char(string="engine Type")
    insurance=fields.Boolean(string="Insurance(true/false)")
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

    add_feature_ids=fields.Many2many('autoalter.feature',string="Add features")