from odoo import models, fields

class Book(models.Model):
    _name = "bookstore.author"
    _description = "Author Details"
    _log_access = False

   
    #name = fields.Char("Author Name" , required=True)
    name = fields.Many2one("res.partner", string="Autor Name", required=True)
    author_ids = fields.One2many("bookstore.book" , "author_id", string="Authors")
   
#     _sql_constraints = [
#             ('check_author', 'UNIQUE(name)', "Author name must be unique!!")
#     ]