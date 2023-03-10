from odoo import models,fields

class AutoalterExteriorMaterials(models.Model):
    _name='autoalter.custprice'
    _description='custom price'
    _rec_name='price'

    price=fields.Float(string="Ex[ected price")
    order_price_ids=fields.Many2many('autoalter.order',string="Expected price")
    cust_price_ids=fields.Many2many('autoalter.customizer',string="Expected price")

    id_order=fields.Integer(string="order id")
    id_cust=fields.Integer(string="customizer id")