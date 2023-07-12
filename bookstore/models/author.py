from odoo import models, fields, api

class Book(models.Model):
    _name = "bookstore.author"
    _description = "Author Details"
    _log_access = False

   
    name = fields.Char("Author Name" , required=True)
    author_ids = fields.One2many("bookstore.book" , "author_id", string="Authors")
   
    _sql_constraints = [
            ('check_author', 'UNIQUE(name)', "Author name must be unique!!")
    ]