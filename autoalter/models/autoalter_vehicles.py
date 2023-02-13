
from odoo import models,fields
from datetime import datetime

class AutoalterVehicles(models.Model):
    _name='autoalter.vehicles'
    _description='show vehicles'
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
    veh_price=fields.Integer(string="Price")
    engine_type=fields.Char(string="Engine Type")
    displacement=fields.Float(string="Displacement(cc)")
    max_power=fields.Char(string="Max Power")
    max_torque=fields.Char(string="Max tourqe")
    no_cylinder=fields.Integer(string="No of Cylinder")
    trans_type=fields.Char(string="Transmission Type")
    gear_box=fields.Integer(string="Gear Box")
    fuel_type=fields.Char(string="Fuel Type")
    mileage=fields.Float(string="Mileage(kmpl)")
    tank_cap=fields.Float(string="Fuel Tank Capacity(liter)")
    other_fuel_type=fields.Selection(string="Other Fuel Type",
        selection=[('petrol','Petrol'),('disel','Disel'),('lpg','LPG'),('cng','CNG')])
    f_suspen=fields.Char(string="Front Suspension")
    r_suspen=fields.Char(string="Rear Suspention")
    ster_col=fields.Char(string="Steering Column")
    turn_rad=fields.Float(string="Turning Radius(meter)")
    f_break_typ=fields.Char(string="Front Break Type")
    r_break_typ=fields.Char(string="Rear Break Type")
    length=fields.Integer(string="Length(mm)")
    width=fields.Integer(string="Width(mm)")
    height=fields.Integer(string="Height(mm)")
    seat_capcty=fields.Integer(string="Seating capacity")
    wheelbase=fields.Integer(string="Wheel Base(mm)")
    kerb_weight=fields.Integer(string="Kerb Weight(kg)")
    no_door=fields.Integer(string="No of Doors")
    tyre_size=fields.Char(string="Tyre Size")
    tyre_typ=fields.Char(string="Tyre Type")
    wheel_size=fields.Integer(string="Wheel Size(rim)")
    cmp_add=fields.Char(string="Address")
    cmp_email=fields.Char(string="Email id")
    cmp_contact=fields.Integer(string="Contact no")
    cmp_year=fields.Selection(selection='years_selection',
        string="Year of Origin")
    def years_selection(self):
        year_list=[]
        for y in range(datetime.now().year-50, datetime.now().year):
            year_list.append((str(y), str(y)))
        return year_list

    cun_origin=fields.Char(string="Country of Origin")
    
