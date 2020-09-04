# -*- coding: utf-8 -*-
from odoo import http


class TodoTask(http.Controller):
    @http.route('/todo_task/todo_task/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/todo_task/todo_task/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('todo_task.listing', {
            'root': '/todo_task/todo_task',
            'objects': http.request.env['todo_task.todo_task'].search([]),
        })

    @http.route('/todo_task/todo_task/objects/<model("todo_task.todo_task"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('todo_task.object', {
            'object': obj
        })
