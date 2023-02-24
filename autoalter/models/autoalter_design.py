from odoo import api,models,fields
import odoo.exceptions

class AutoalterDesign(models.Model):
    _name='autoalter.design'
    _description='show designs'
    _rec_name="design_name"
    
    design_name=fields.Char(string="Design name")
    design_img=fields.Image(string="Design Image",
        required=True)
    
    des_price=fields.Float(string="Price",
        required=True)
    design_name_id=fields.Many2one('autoalter.customizer',string="Designer Name")

    
    des_gmail=fields.Char(string="Gmail",
        required=True,
        compute="_compute_email")

    @api.depends("design_name_id.cust_emial")
    def _compute_email(self):
        for record in self:
            record.des_gmail=self.design_name_id.cust_emial
    
    
    
