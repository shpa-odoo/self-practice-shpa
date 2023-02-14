from odoo import models,fields

class AutoalterInteriorMaterials(models.Model):
    _name='autoalter.interior.materials'
    _description='interior materials'
    _rec_name="interior_mat"

    interior_mat=fields.Char(string="Interier material and feature")