
from odoo import models,fields

class AutoalterVehicles(models.Model):
    _name='autoalter.vehicles'
    _description='show vehicles'
    vehicle_img=fields.Image()
    comp_name=fields.Char(string="Company Name")
    vehicle_type=fields.Selection(selection=[('4-wheelers','4-Wheelers'),
        ('2-wheelers','2-Wheelers'),
        ('3-wheelers','3-Wheelers'),
        ('>4-wheelers','>4-Wheelers')],
        string="Type")
    model=fields.Char(string="Model Name")
    menufect_id=fields.Char(string="Menufecture id",
        copy=False,
        required=True)
    price=fields.Integer(string="Price")
    description=fields.Char(string="Discription")

