from odoo import models, fields

class BookType(models.Model):
     _name = "bookstore.book.type"
     _description = "Type of Books"
     _log_access = False
     # _rec_name= "tag_ids"
     Active = False

     name = fields.Selection([('f','Fiction'),('n','Non-Fiction')],"Categotry Name", default='f')
     book_type = fields.Char("Book Type")
     # tag_ids = fields.Many2many("bookstore.tag", string="Tags")
     book_ids = fields.One2many("bookstore.book" , "book_type_id" ,string="Types")