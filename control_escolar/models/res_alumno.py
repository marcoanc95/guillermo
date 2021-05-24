# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResAlumno(models.Model):
     _name = 'res.alumno'
     _inherit = ['mail.thread', 'mail.activity.mixin']

     name = fields.Char(string="Nombre")
     edad = fields.Integer(string="Edad")
     promedio = fields.Float(string="Promedio")
     