from odoo import models, fields, api

class Book(models.Model):
    _name = "bookstore.author"
    _description = "Author Details"
    _log_access = False

    first_name = fields.Char("First Name", required= True)
    last_name = fields.Char("Last Name", required= True)
    full_name = fields.Char("Full Name", compute="_compute_full_name", readonly=False)
   # book_ids = fields.Many2many()
    
    @api.depends('first_name','last_name')
    def _compute_full_name(self):
        for i in self:
          i.full_name = i.first_name + ' ' + i.last_name