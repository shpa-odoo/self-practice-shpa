from odoo import fields,models,api

class AutoalterAuctconnect(models.Model):
    _name="autoalter.auctconnect"
    _description="connecter"
    _rec_name="m_name"

    auctconct_ids=fields.One2many('autoalter.auctprice','auctprice_id')
    act_id=fields.Integer(string="auct id")
    c_name=fields.Char(string="Company Name")
    m_name=fields.Char(string="Model name")
    d_purchase=fields.Date(string="Purchase date")
    s_price=fields.Float(string="starting price")
    l_dt=fields.Datetime(string="last date")
    auct_i=fields.Image(string="vehicle")
    best_price=fields.Float(compute="_offer_price",string="Best price")

    @api.depends("auctconct_ids.price")
    def _offer_price(self):
	    for record in self:
             if record.auctconct_ids:
                   record.best_price = max(record.auctconct_ids.mapped('price'))
             else:
                   record.best_price = 0
             print(record.best_price)
		    
