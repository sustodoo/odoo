# -*- coding: utf-8 -*-

from odoo import models, fields, api

class collage(models.Model):
    _name = 'collage.collage'

    name = fields.Char('Name')
    code = fields.Char(string="Code", required=False, )
    dean_id = fields.Many2one(comodel_name="collage.employee", string="Dean", required=False, )


class employee(models.Model):
    _name = 'collage.employee'

    name = fields.Char('Name')
    code = fields.Char('Code')
    type = state = fields.Selection(string="", selection=[('academic', 'Academic'), ('admin', 'Administrative'),('workers','Workers') ], required=False, )
    hiring_date = fields.Date(string="Hiring Date", required=False, )
    collage_id =fields.Many2one(comodel_name="collage.collage", string="Collage", required=False, )


