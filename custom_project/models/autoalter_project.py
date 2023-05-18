from odoo import models,api,Command

class AutoalterProject(models.Model):
    _inherit="autoalter.order"

    @api.model
    def create(self,vals):
                print(self.offer_ids.partner_id)
                project=self.env['project.project'].create({
                    'name':"custom",
                    'task_ids':[
                    (0,0,{
                        'name':"demo",
                    })
                    ]
                    
                
                })
                
                return super(models.Model,self).create(vals)
