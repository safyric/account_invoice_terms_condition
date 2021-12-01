from odoo import fields, models, api, _

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    comment = fields.Html(string='Terms and conditions', default=_default_comment)

    @api.model
    def _default_comment(self):
        return self.env['ir.config_parameter'].sudo().get_param('account.use_invoice_comment') and self.env.user.company_id.invoice_comment or ''
