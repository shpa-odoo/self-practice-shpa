from odoo import models,fields

class AutoalterOffer(models.Model):
    _name="autoalter.offer"
    _description="cust offer"
    _rec_name="price"

    price=fields.Float(string="Price")
    status=fields.Selection(selection=[('accepted','Accepted'),('refused','Refused')],
		copy=False,
		string="status")
    partner_id=fields.Many2one('autoalter.customizer',
        string="Coustomizer",
        required=True)
    exp=fields.Char(related="partner_id.cust_exp",
                    string="experience")
    type=fields.Many2many(related="partner_id.cust_typ_ids")
    pof_id=fields.Many2one("autoalter.order")
    def action_accept(self):
      for record in self:
        record.status="accepted"
        record.pof_id.state="order"
        record.pof_id.cust_total_price=record.price
        record.partner_id.cust_avil=False

    def action_refuse(self):
      for record in self:
        record.status="refused"