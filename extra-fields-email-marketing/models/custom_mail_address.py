from odoo import fields, models, api


class CustomMailAddress(models.Model):
    """Adding custom address
       fields"""
    _inherit = 'mailing.contact'

    street = fields.Char(string=' Street ',
                         required=True,
                         help='Street address')
    city = fields.Char(string=' City ',
                       required=True,
                       help='City')
    state_id = fields.Many2one(
        'res.country.state',
        string='Province',
        default=lambda self: self.env['res.country.state'].search([('code', '=', 'NB')], limit=1),
        help='Select the state for the contact.'
    )
    country_id = fields.Many2one(
        'res.country',
        string='Country',
        default=lambda self: self.env['res.country'].search([('code', '=', 'CA')], limit=1),
        help='Select the country for the contact.'
    )
    zip_code = fields.Char(string=' Zip Code ',
                           required=True,
                           help='Zip Code')

    @api.onchange('country_id')
    def onchange_country_id(self):
        """Update state_id based on selected country"""
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}
