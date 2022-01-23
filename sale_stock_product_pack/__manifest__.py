# Copyright 2019 NaN (http://www.nan-tic.com) - Àngel Àlvarez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale stock product Pack',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'summary':
        'This module allows you to sale and ship non-detailed '
        'product packs',
    'website': 'https://github.com/OCA/product-pack',
    'author': 'DEC, '
              'Odoo Community Association (OCA)',
    'maintainers': [],
    'license': 'AGPL-3',
    'depends': [
        'sale_stock',
        'sale_product_pack',
        'stock_product_pack',
    ],
    'data': ['views/product_pack_line_views.xml', ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
