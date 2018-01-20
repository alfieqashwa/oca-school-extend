# -*- coding: utf-8 -*-
from odoo import http

# class OcaSekolahEvent(http.Controller):
#     @http.route('/oca_sekolah_event/oca_sekolah_event/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oca_sekolah_event/oca_sekolah_event/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oca_sekolah_event.listing', {
#             'root': '/oca_sekolah_event/oca_sekolah_event',
#             'objects': http.request.env['oca_sekolah_event.oca_sekolah_event'].search([]),
#         })

#     @http.route('/oca_sekolah_event/oca_sekolah_event/objects/<model("oca_sekolah_event.oca_sekolah_event"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oca_sekolah_event.object', {
#             'object': obj
#         })