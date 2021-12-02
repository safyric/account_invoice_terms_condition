{
    'name': 'Account Invoice Default Terms Conditions',
    'summary': """
        This module allows account invoice default terms & conditions""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Safyric Co., Ltd.',
    'website': 'https://www.safyric.com',
    'depends': [
        'account',
    ],
    'data': [
        'views/res_config_settings.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
}
