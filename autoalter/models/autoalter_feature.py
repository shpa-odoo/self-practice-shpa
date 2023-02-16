from odoo import models,fields

class AutoalterFeature(models.Model):
    _name='autoalter.feature'
    _description='feature type'
    _rec_name="feature_typ"

    
    feature_typ=fields.Char(string="Feature Types")