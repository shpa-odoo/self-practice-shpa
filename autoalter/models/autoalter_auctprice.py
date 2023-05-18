from odoo import fields,models,api
import odoo.exceptions

class AutoalterAuctprice(models.Model):
    _name="autoalter.auctprice"
    _description="auction price"

    buyer_id=fields.Many2one('res.partner')
    eml=fields.Char(related="buyer_id.email")
    mobile_no=fields.Char(related="buyer_id.phone")
    price=fields.Float(string="price",required=True)

    auctprice_id=fields.Many2one('autoalter.auctconnect')

    @api.model
    def create(self,vals):
      count= self.env['autoalter.auctconnect'].browse(vals["auctprice_id"])
      if vals['price'] <= count.best_price:
        raise odoo.exceptions.UserError("You cannot create lower price than present price")
      return super(AutoalterAuctprice,self).create(vals)
