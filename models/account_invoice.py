from odoo import fields, models, api, _

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    comment = fields.Html(string='Terms and conditions')
