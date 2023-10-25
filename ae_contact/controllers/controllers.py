# -*- coding: utf-8 -*-
# from odoo import http


# class AeContact(http.Controller):
#     @http.route('/ae_contact/ae_contact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ae_contact/ae_contact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ae_contact.listing', {
#             'root': '/ae_contact/ae_contact',
#             'objects': http.request.env['ae_contact.ae_contact'].search([]),
#         })

#     @http.route('/ae_contact/ae_contact/objects/<model("ae_contact.ae_contact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ae_contact.object', {
#             'object': obj
#         })
