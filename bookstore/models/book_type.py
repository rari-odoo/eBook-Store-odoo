from odoo import models, fields

class BookType(models.Model):
     _name = "bookstore.book.type"
     _description = "Type of Books"
     _log_access = False
     Active = False

     name = fields.Char("Tag Name", required=True)
     category =fields.Selection([('f','Fiction'),('n','Non-Fiction')],"Categotry Name", default='f')
     color = fields.Integer("Color")
     # name = fields.Many2many("bookstore.tag", string="Tags")
     book_ids = fields.One2many("bookstore.book" , "book_type_id" ,string="Types")