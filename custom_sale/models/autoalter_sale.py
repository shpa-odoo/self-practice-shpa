from odoo import models,api

class AutoalterProject(models.Model):
    _inherit="autoalter.order"

    
    def action_buy(self):
        
            self.env['sale.order'].create({
                'partner_id':self.select_customer_id.id,
                
            })
        
            return super().action_buy()
    