from odoo import models,fields

class InheritValue(models.Model):
    #_inherit="autoalter.vehicles"
    _description="inherit vehicle value"

    
    
    # self.env['autoalter.order'].create({
    #         'select_vehicle_ids':[(4, [event_id.id])]  
                
    #     })