# -*- coding: utf-8 -*-
{
    'name': "oca_sekolah_evaluasi",

    'summary': """
        Extend OCA-School-Evaluation Apps""",

    'description': """
        The purpose is to extenf OCA-School-Evaluation Education Management System
    """,

    'author': "Alfie Qashwa Habib",
    'website': "https://github.com/alfieqashwa",
    'category': 'School Management',
    'version': '10.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['school_evaluation'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto-install': False,
}