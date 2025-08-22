# -*- coding: utf-8 -*-
# from odoo import http


# class MadarPes(http.Controller):
#     @http.route('/madar_pes/madar_pes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madar_pes/madar_pes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('madar_pes.listing', {
#             'root': '/madar_pes/madar_pes',
#             'objects': http.request.env['madar_pes.madar_pes'].search([]),
#         })

#     @http.route('/madar_pes/madar_pes/objects/<model("madar_pes.madar_pes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madar_pes.object', {
#             'object': obj
#         })

