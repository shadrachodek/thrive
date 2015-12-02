# -*- coding: utf-8 -*-
from openerp import http

# class Thrivebase(http.Controller):
#     @http.route('/thrivebase/thrivebase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thrivebase/thrivebase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('thrivebase.listing', {
#             'root': '/thrivebase/thrivebase',
#             'objects': http.request.env['thrivebase.thrivebase'].search([]),
#         })

#     @http.route('/thrivebase/thrivebase/objects/<model("thrivebase.thrivebase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thrivebase.object', {
#             'object': obj
#         })