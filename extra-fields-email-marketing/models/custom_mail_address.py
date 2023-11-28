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
    province = fields.Char(string=' Province ',
                           required=True,
                           default='New Brunswick',
                           readonly=True,
                           help='Province')
    country = fields.Char(string=' Country ',
                          required=True,
                          default='Canada',
                          readonly=True,
                          help='Country')
    zip_code = fields.Char(string=' Zip Code ',
                           required=True,
                           help='Zip Code')
