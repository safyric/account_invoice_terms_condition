{
    'name': 'Account Invoice Default Terms Conditions',
    'summary': """
        This module allows account invoice default terms & conditions""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Safyric Co., Ltd.',
    'website': 'https://www.safyric.com',
    'images': ['static/description/banner.png'],
    'depends': [
        'account',
    ],
    'data': [
        'views/res_config_settings.xml',
        'views/account_invoice_template.xml',
    ],
}
