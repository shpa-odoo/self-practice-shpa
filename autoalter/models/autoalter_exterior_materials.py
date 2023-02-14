from odoo import models,fields

class AutoalterExteriorMaterials(models.Model):
    _name='autoalter.exterior.materials'
    _description='interior materials'
    _rec_name='exterior_mat'

    exterior_mat=fields.Char(string="Exterier material and feature")