# -*- coding: utf-8 -*-
from odoo import http

# class OcaSekolahEvaluasi(http.Controller):
#     @http.route('/oca_sekolah_evaluasi/oca_sekolah_evaluasi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oca_sekolah_evaluasi/oca_sekolah_evaluasi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oca_sekolah_evaluasi.listing', {
#             'root': '/oca_sekolah_evaluasi/oca_sekolah_evaluasi',
#             'objects': http.request.env['oca_sekolah_evaluasi.oca_sekolah_evaluasi'].search([]),
#         })

#     @http.route('/oca_sekolah_evaluasi/oca_sekolah_evaluasi/objects/<model("oca_sekolah_evaluasi.oca_sekolah_evaluasi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oca_sekolah_evaluasi.object', {
#             'object': obj
#         })