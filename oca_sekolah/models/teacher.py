# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SchoolTeacher(models.Model):
    _inherit = 'school.teacher'

    school_id = fields.Many2one(string="School")