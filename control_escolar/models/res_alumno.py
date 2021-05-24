# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResAlumno(models.Model):
     _name = 'res.alumno'
     _inherit = ['mail.thread', 'mail.activity.mixin']

     name = fields.Char(string='Nombre', copy=False, index=True, default=lambda self: _('New'))
     edad = fields.Integer(string="Edad")
     promedio = fields.Float(string="Promedio")

     @api.model
     def create(self, vals):
          if vals.get('name', _('New')) == _('New'):
               vals['name'] = self.env['ir.sequence'].next_by_code('installed.services') or _('New')

          result = super(ResAlumno, self).create(vals)
          return result
     