# -*- coding: utf-8 -*-
{
    'name': "Madar PES – Partial & Multi-word Product Search",

    'summary': "Unordered multi-word and partial product search in POS, Sales & Stock (supports Arabic & English).",

    'description': """
This module improves Odoo product search by adding:
- Partial search (by any part of the product name).
- Unordered multi-word search.
- Works in Point of Sale, Sales, and Stock.
- Supports both Arabic and English search terms.
    """,

    'author': "sarareda-dev",
    'website': "https://github.com/sarareda-dev/odoo-18",

    'category': 'Sales/Point of Sale',
    'version': '18.0.1.0.0',

    'license': 'LGPL-3',

    # dependencies
    'depends': ['base', 'product', 'point_of_sale', 'stock'],

    # data files
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    # assets
    'assets': {
        'point_of_sale._assets_pos': [
            'madar_pes/static/src/js/search_patch.js',
        ],
    },

    'demo': [
        'demo/demo.xml',
    ],

    'images': [
        'static/description/1.jpeg',
        'static/description/2.jpeg',
        'static/description/3.jpeg',
    ],

    'installable': True,
    'application': False,

    # 🟢 السعر والعملة (Odoo Apps)
    'price': 150.0,
    'currency': 'USD',
}
