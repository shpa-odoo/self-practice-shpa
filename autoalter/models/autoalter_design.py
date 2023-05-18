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
    _sql_constraints=[
		('check_des_price','CHECK (des_price>0)','Price must be positive.')
	]
    design_name_id=fields.Many2one('autoalter.customizer',string="Design by",required=True)
    des_gmail=fields.Char(string="Gmail",
        related="design_name_id.cust_emial")
    
    def action_des_order(self):
        # self.ensure_one()
        result={
            "type":"ir.actions.act_window",
            "res_model":"autoalter.order",
            "view_mode":'form',
            "name":"open design page",
            "context":{"default_buy_design":True,
                       "default_select_design_ids":[(4, [self.id])]
                       },
        }
        return result
