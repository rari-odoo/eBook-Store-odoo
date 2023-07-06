from odoo import models, fields

class BookType(models.Model):
     _name = "bookstore.book.type"
     _description = "Type of Books"
     _log_access = False
     Active = False

     name = fields.Char("Type" , required=True)
     book_ids = fields.One2many("bookstore.book" , "book_type_id" ,string="Types")