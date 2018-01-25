# See LICENSE file for full copyright and licensing details.

{
    'name': 'SO - Product Price Check',
    'version': '11.0.1.0.0',
    'category': 'Sales Management',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'summary': '''Restrict sales on 0 value.
                  This module restricts a user from
                  confirming a Sale Order/Quotation.
                  This module restricts a user from
                  confirming a Sale Order/Quotation
                  if it contains products having sale price Zero.
                ''',
    'license': 'AGPL-3',
    'maintainer': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',
    'depends': [
        'sale',
    ],
    'images': [
        'static/description/PriceCheck.png',
    ],
    'installable': True,
}
