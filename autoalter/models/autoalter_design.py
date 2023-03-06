from odoo import api,models,fields
import odoo.exceptions

class AutoalterDesign(models.Model):
    _name='autoalter.design'
    _description='show designs'
    _rec_name="design_name"
    

    is_favorite=fields.Boolean(string="Fevorite")
    design_name=fields.Char(string="Design name")
    design_img=fields.Image(string="Design Image",
        required=True)
    
    des_price=fields.Float(string="Price",
        required=True)
    design_name_id=fields.Many2one('autoalter.customizer',string="Design by")

    
    des_gmail=fields.Char(string="Gmail",
        related="design_name_id.cust_emial")

    # @api.depends("design_name_id.cust_emial")
    # def _compute_email(self):
    #     for record in self:
    #         record.des_gmail=self.design_name_id.cust_emial
    
    
    def action_des_order(self):
        # self.ensure_one()
        # ord=self.env['autoalter.order']
        # ord["buy_design"]=True
        
        #ord.select_vehicle_ids=self.id
        result={
            "type":"ir.actions.act_window",
            "res_model":"autoalter.order",
            "view_mode":'form',
            "name":"open design page",
            "context":{"buy_design":True},
        }
        return result
