from odoo import models,fields

class AutoalterCustomizerType(models.Model):
    _name='autoalter.customizer.type'
    _description='coustomizer type'
    _rec_name='customizer_typ'

    customizer_typ=fields.Char(string="Customizer Types")