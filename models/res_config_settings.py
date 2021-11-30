from odoo import fields, models

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    invoice_comment = fields.Html(
        related='company_id.invoice_comment',
        string="Invoice Terms & Conditions",
        default_model="account.invoice",
        readonly=False)

    use_iniivoice_comment = fields.Boolean(
        string='Use Invoice Default Terms & Conditions',
        config_parameter='account.use_invoice_comment')
