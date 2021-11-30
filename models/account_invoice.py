from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    comment = fields.Html('Additional Information', readonly=True, states={'draft': [('readonly', False)]})
