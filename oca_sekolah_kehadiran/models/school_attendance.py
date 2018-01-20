# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AttendanceSheet(models.Model):
    _inherit = 'attendance.sheet'

    user_id = fields.Many2one(string='Teacher')


class DailyAttendance(models.Model):
    _inherit = 'daily.attendance'

    user_id = fields.Many2one(string='Teacher')

