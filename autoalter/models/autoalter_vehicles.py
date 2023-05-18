
from odoo import models,fields
from datetime import datetime

class AutoalterVehicles(models.Model):
    _name='autoalter.vehicles'
    _description='show vehicles'
    _rec_name="model"

    is_favorite=fields.Boolean(string="favorite")
    vehicle_img=fields.Image(string="Vehicle Image",
                             required=True)
    comp_name=fields.Char(string="Company Name",
                          required=True)
    vehicle_type=fields.Selection(selection=[('car','Car'),
        ('scooter','Scooter'),
        ('bike','Bike'),
        ('truck','Truck'),
        ('bicycle','Bicycle'),
        ('bus','Bus')],
        string="Type")
    model=fields.Char(string="Model Name",required=True)
    veh_price=fields.Float(string="Price",
                           required=True)
    _sql_constraints=[
		('check_price','CHECK (veh_price>0)','Price must be positive.')
	]
    engine_type=fields.Char(string="Engine Type",required=True)
    displacement=fields.Char(string="Displacement(cc)",required=True)
    max_power=fields.Char(string="Max Power",required=True)
    max_torque=fields.Char(string="Max tourqe",required=True)
    no_cylinder=fields.Char(string="No of Cylinder",required=True)
    trans_type=fields.Char(string="Transmission Type",required=True)
    gear_box=fields.Char(string="Gear Box",required=True)
    fuel_type=fields.Selection(string="Fuel Type",
        selection=[('petrol','Petrol'),('disel','Disel'),('lpg','LPG'),('cng','CNG')])
    mileage=fields.Char(string="Mileage(kmpl)",required=True)
    tank_cap=fields.Char(string="Fuel Tank Capacity(liter)",required=True)
    other_fuel_type=fields.Selection(string="Other Fuel Type",
        selection=[('petrol','Petrol'),('disel','Disel'),('lpg','LPG'),('cng','CNG')])
    f_suspen=fields.Char(string="Front Suspension")
    r_suspen=fields.Char(string="Rear Suspention")
    ster_col=fields.Char(string="Steering Column")
    turn_rad=fields.Char(string="Turning Radius(meter)",required=True)
    f_break_typ=fields.Char(string="Front Break Type",required=True)
    r_break_typ=fields.Char(string="Rear Break Type",required=True)
    length=fields.Char(string="Length(mm)")
    width=fields.Char(string="Width(mm)")
    height=fields.Char(string="Height(mm)")
    seat_capcty=fields.Char(string="Seating capacity")
    wheelbase=fields.Char(string="Wheel Base(mm)",required=True)
    kerb_weight=fields.Char(string="Kerb Weight(kg)",required=True)
    no_door=fields.Char(string="No of Doors")
    tyre_size=fields.Char(string="Tyre Size")
    tyre_typ=fields.Char(string="Tyre Type")
    wheel_size=fields.Char(string="Wheel Size(rim)")
    cmp_add=fields.Char(string="Address")
    cmp_email=fields.Char(string="Email id")
    cmp_contact=fields.Char(string="Contact no")
    cmp_year=fields.Selection(selection='years_selection',
        string="Year of Origin")
    def years_selection(self):
        year_list=[]
        for y in range(datetime.now().year-50, datetime.now().year):
            year_list.append((str(y), str(y)))
        return year_list
    
    cun_origin=fields.Char(string="Country of Origin")

    interior_ids=fields.Many2many('autoalter.interior.materials',string="Interior",required=True)
    exterior_ids=fields.Many2many('autoalter.exterior.materials',string="Exterior",required=True)
    feature_ids=fields.Many2many('autoalter.feature',string="Features",required=True)

    
    def action_veh_order(self):
        self.ensure_one()
        
        # ord.select_vehicle_ids=self.id
        # ord=self.env['autoalter.order']
        # ord.write({'select_vehicle_ids': [(4, [active_id])] }) 
        result={
            "type":"ir.actions.act_window",
            "res_model":"autoalter.order",
            "view_mode":'form',
            "name":"open veh page",
            "context":{"default_buy_vehicle":True,
                       "default_select_vehicle_ids":[(4, [self.id])]
                    },
        }
        return result
        