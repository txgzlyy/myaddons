# -*- coding: utf-8 -*-
{
    'name': "engineering",
    'description': """
        工程部物料管理
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
}
