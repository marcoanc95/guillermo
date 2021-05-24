# -*- coding: utf-8 -*-
{
    'name': "Control escolar",

    'summary': """
        Control escolar - Primaria""",

    'description': """
        Control escolar - Primaria
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/res_alumno_menu.xml',
        'views/res_alumno.xml',
    ],
}