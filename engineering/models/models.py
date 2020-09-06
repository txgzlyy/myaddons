# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DredgeList(models.Model):
    _name = "eng.dredge"
    _description = "疏浚物料装载单"

    sand_h = fields.Integer(string="高级砂(kg)")
    sand_m = fields.Integer(string="中级砂(kg)")
    sand_d = fields.Integer(string="低级砂(kg)")
    dredge_time = fields.Datetime(string="装载时间")

    audit_id = fields.Many2one("eng.audit", string="疏浚物料审核单")


class TakeoverList(models.Model):
    _name = 'eng.takeover'
    _description = '接管物料装载单'

    sand_h = fields.Integer(string="高级砂(kg)")
    sand_m = fields.Integer(string="中级砂(kg)")
    sand_d = fields.Integer(string="低级砂(kg)")
    takeover_time = fields.Datetime(string="接管装载时间")

    audit_id = fields.Many2one("eng.audit", string="接管物料审核单")


class MaterialAudit(models.Model):
    _name = 'eng.audit'
    _description = '物料审核单'

    name = fields.Datetime(string="日期")
    dredge_id = fields.One2many("eng.dredge", 'audit_id', string='疏浚物料装载单')
    takeover_id = fields.One2many("eng.takeover", 'audit_id', string='接管物料装载单')