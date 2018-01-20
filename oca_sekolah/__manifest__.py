# -*- coding: utf-8 -*-
{
    'name': "oca_sekolah",

    'summary': """
        Extend OCA-School Apps""",

    'description': """
        The purpose is to extenf OCA-School Education Management System
    """,

    'author': "Alfie Qashwa Habib",
    'website': "https://github.com/alfieqashwa",
    'category': 'School Management',
    'version': '10.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['school'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/school_view.xml',
        'views/student_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto-install': False,
}