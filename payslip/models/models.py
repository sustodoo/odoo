# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payslip(models.Model):
    _name = 'payslip.payslip'

    name = fields.Char('Name')
    code = fields.Char('Code')
    employee_type = fields.Selection(string="", selection=[('academic', 'Academic'), ('admin', 'Administrative'),
                                                           ('workers', 'Workers')], required=False, )
    step_ids = fields.One2many(comodel_name="payslip.payslip.step", inverse_name="payslip_id", string="Steps",
                               required=False, )


class Payslip_Step(models.Model):
    _name = 'payslip.payslip.step'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char('Name')
    code = fields.Char('Code')
    employee_id = fields.Many2one(comodel_name="collage.employee", string="Employee", required=False, )
    payslip_id = fields.Many2one(comodel_name="payslip.payslip", string="payslip", required=False, )


class Allowance(models.Model):
    _name = 'payslip.allowance'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char('Name')
    code = fields.Char('Code')
    employee_type = fields.Selection(string="", selection=[('academic', 'Academic'), ('admin', 'Administrative'),
                                                           ('workers', 'Workers')], required=False, )

class StepsAllowance(models.Model):
    _name = 'payslip.stepsallowance'
    _description = 'New Description'

    allowce_id = fields.Many2one(comodel_name="payslip.allowance", string="Allowance", required=False, )
    step_id = fields.Many2one(comodel_name="payslip.payslip.step", string="Step", required=False, )
    amount = fields.Float(string="Amount", required=False, )


class Employee(models.Model):
    _name = 'collage.employee'
    _inherit = 'collage.employee'

    payslip_id = fields.Many2one(comodel_name="payslip.payslip_Step", string="Payslip", required=False, )
    step_ids = fields.One2many(comodel_name="payslip.payslip.step", inverse_name="employee_id", string="",
                               required=False, )
    salary = fields.Float(string="Salary", required=False, )
