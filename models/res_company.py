from odoo import fields, models


class ResCompany(models.Model):

    _inherit = 'res.company'

    comment = fields.Html(
        string='Invoice Default Terms and Conditions',
        translate=True)
