# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolEvaluation(models.Model):
    _inherit = "school.evaluation"

    type = fields.Selection([('student', 'Student'),
                         ('faculty', 'Teacher')],
                        'User Type', required=True,
                        help="Type of evaluation")


class SchoolEvaluationTemplate(models.Model):
	_inherit = "school.evaluation.template"

	type = fields.Selection([('faculty', 'Teacher'), ('student', 'Student')],
    	                    'User Type', required=True, default='faculty',
        	                help="Type of Evaluation")