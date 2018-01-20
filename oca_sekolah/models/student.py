# -*- coding: utf-8 -*-
from odoo import models, fields, api


class StudentStudent(models.Model):
	_inherit = 'student.student'

	middle = fields.Char(required=False)