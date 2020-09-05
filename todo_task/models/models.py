# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoCategory(models.Model):
    _name = "todo.category"
    _description = "待办事项分类"

    name = fields.Char(string="类别名称", required=True)
    task_id = fields.One2many("todo_task.todo_task", "category_id", string="待办事件")
    task_num = fields.Integer(string="代办事件数量", compute="_compute_task_num")

    @api.depends("task_id")
    @api.multi
    def _compute_task_num(self):
        for res in self:
            res.task_num = len(res.task_id)


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = '待办事件详情'

    name = fields.Char(string="任务名")
    description = fields.Text(string='描述')
    is_done = fields.Boolean(string="是否完成")
    emergency_status = fields.Selection([("todo", "代办"), ("emergency", "紧急")], default="todo", string='紧急情况')
    overdue_time = fields.Datetime(string="过期时间")
    is_overdue = fields.Boolean(string="是否过期", compute="_compute_is_overdue")

    category_id = fields.Many2one("todo.category", string="类别")

    @api.depends("overdue_time")
    @api.multi
    def _compute_is_overdue(self):
        for res in self:
            if res.overdue_time:
                res.is_overdue = res.overdue_time < fields.Datetime.now()
            else:
                res.is_overdue = False
