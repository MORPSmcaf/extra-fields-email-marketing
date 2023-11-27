from odoo import fields, models


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
    state = fields.Char(string=' State ',
                        required=True,
                        help='State')
    zip_code = fields.Char(string=' Zip Code ',
                           required=True,
                           help='Zip Code')
