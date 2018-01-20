# -*- coding: utf-8 -*-
from odoo import http

# class OcaSekolahKehadiran(http.Controller):
#     @http.route('/oca_sekolah_kehadiran/oca_sekolah_kehadiran/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oca_sekolah_kehadiran/oca_sekolah_kehadiran/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oca_sekolah_kehadiran.listing', {
#             'root': '/oca_sekolah_kehadiran/oca_sekolah_kehadiran',
#             'objects': http.request.env['oca_sekolah_kehadiran.oca_sekolah_kehadiran'].search([]),
#         })

#     @http.route('/oca_sekolah_kehadiran/oca_sekolah_kehadiran/objects/<model("oca_sekolah_kehadiran.oca_sekolah_kehadiran"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oca_sekolah_kehadiran.object', {
#             'object': obj
#         })