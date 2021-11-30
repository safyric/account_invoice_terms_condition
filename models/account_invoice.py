from odoo import api, fields, models, _


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    comment = fields.Html(string='Additional Information', default=_default_comment)

    @api.model
    def _default_comment(self):
        return self.env['ir.config_parameter'].sudo().get_param('account.use_invoice_comment') and self.env.user.company_id.invoice_comment or ''
