from odoo import fields, models

class ResourceMail(models.Model):
    _inherit = 'mailing.contact'

    res_street = fields.Char(string='Street', help='Street address')
    res_city = fields.Char(string='City', help='City')
    res_state = fields.Char(string='State', help='State')
