from odoo import models,fields,Command

class AutoalterWizard(models.TransientModel):
    _name="autoalter.wizard"
    _description="offer wizard"

    price=fields.Float(string="Price")
    status=fields.Selection(selection=[('accepted','Accepted'),('refused','Refused')],
		copy=False,
		string="status")
    partner_id=fields.Many2one('autoalter.customizer',
        string="Coustomizer",
        required=True)
    
    def action_do_something(self):
        offer = self.env['autoalter.order'].browse(self.env.context.get('active_ids'))
        for record in offer:
            if record.buy_custom == True and record.user_discrip :
                record.write({
                    'offer_ids':[
                        Command.create({
                            'price':self.price,
                            'partner_id':self.partner_id.id
                        })  
                    ]
                })  
        return {'type': 'ir.actions.act_window_close'}
    
    
