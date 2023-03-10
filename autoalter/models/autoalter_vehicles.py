
from odoo import models,fields
from datetime import datetime

class AutoalterVehicles(models.Model):
    _name='autoalter.vehicles'
    _description='show vehicles'
    _rec_name="model"

    is_favorite=fields.Boolean(string="favorite")
    vehicle_img=fields.Image(string="Vehicle Image")
    comp_name=fields.Char(string="Company Name")
    vehicle_type=fields.Selection(selection=[('car','Car'),
        ('scooter','Scooter'),
        ('bike','Bike'),
        ('truck','Truck'),
        ('bicycle','Bicycle'),
        ('bus','Bus')],
        string="Type")
    model=fields.Char(string="Model Name")
    veh_price=fields.Float(string="Price")
    engine_type=fields.Char(string="Engine Type")
    displacement=fields.Char(string="Displacement(cc)")
    max_power=fields.Char(string="Max Power")
    max_torque=fields.Char(string="Max tourqe")
    no_cylinder=fields.Char(string="No of Cylinder")
    trans_type=fields.Char(string="Transmission Type")
    gear_box=fields.Char(string="Gear Box")
    fuel_type=fields.Selection(string="Fuel Type",
        selection=[('petrol','Petrol'),('disel','Disel'),('lpg','LPG'),('cng','CNG')])
    mileage=fields.Char(string="Mileage(kmpl)")
    tank_cap=fields.Char(string="Fuel Tank Capacity(liter)")
    other_fuel_type=fields.Selection(string="Other Fuel Type",
        selection=[('petrol','Petrol'),('disel','Disel'),('lpg','LPG'),('cng','CNG')])
    f_suspen=fields.Char(string="Front Suspension")
    r_suspen=fields.Char(string="Rear Suspention")
    ster_col=fields.Char(string="Steering Column")
    turn_rad=fields.Char(string="Turning Radius(meter)")
    f_break_typ=fields.Char(string="Front Break Type")
    r_break_typ=fields.Char(string="Rear Break Type")
    length=fields.Char(string="Length(mm)")
    width=fields.Char(string="Width(mm)")
    height=fields.Char(string="Height(mm)")
    seat_capcty=fields.Char(string="Seating capacity")
    wheelbase=fields.Char(string="Wheel Base(mm)")
    kerb_weight=fields.Char(string="Kerb Weight(kg)")
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

    interior_ids=fields.Many2many('autoalter.interior.materials',string="Interior")
    exterior_ids=fields.Many2many('autoalter.exterior.materials',string="Exterior")
    feature_ids=fields.Many2many('autoalter.feature',string="Features")

    
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
        