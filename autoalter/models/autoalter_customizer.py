from odoo import api,models,fields
import odoo.exceptions

class AutoalterCustomizer(models.Model):
    _name='autoalter.customizer'
    _inherit="model.test"
    _inherit=['mail.thread', 'mail.activity.mixin']
    _description='show customizer'
    _rec_name="cust_name"

    
    cust_name=fields.Char(string="Name",
        required=True)
    cust_img=fields.Image(string="Customizer Image")
    cust_emial=fields.Char(string="Email id",
        required=True)
    cust_no=fields.Char(string="Contact no")
    cust_exp=fields.Char(string="Experience(year)",
        required=True)
    cust_typ_ids=fields.Many2many('autoalter.customizer.type',string="Type",
        required=True)
    
    cust_avil=fields.Boolean(string="Available")
    order_ids=fields.One2many('autoalter.offer',"partner_id",string="Order id")
    
    or_count=fields.Integer(compute="_compute_order",store=True)
    
       
    @api.depends("order_ids")
    def _compute_order(self):
        for record in self:
            if record.order_ids:
                record.or_count=self.env['autoalter.order'].search_count([]) 
            else:
                record.or_count=0
        
    def action_order_cust(self):
        result={
            "type":"ir.actions.act_window",
            "res_model":"autoalter.order",
            "view_mode":'form',
            "name":"open veh page",
            "context":{"default_buy_custom":True
                       },
        }
        return result
    

