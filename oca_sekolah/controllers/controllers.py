# -*- coding: utf-8 -*-
from odoo import http

# class OcaSekolah(http.Controller):
#     @http.route('/oca_sekolah/oca_sekolah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oca_sekolah/oca_sekolah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oca_sekolah.listing', {
#             'root': '/oca_sekolah/oca_sekolah',
#             'objects': http.request.env['oca_sekolah.oca_sekolah'].search([]),
#         })

#     @http.route('/oca_sekolah/oca_sekolah/objects/<model("oca_sekolah.oca_sekolah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oca_sekolah.object', {
#             'object': obj
#         })