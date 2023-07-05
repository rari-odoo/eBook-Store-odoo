from odoo import models, fields

class EstatePropertyType(models.Model):
     _name = "bookstore.book.type"
     _description = "Type of Books"
     _log_access = False
     Active = False

     name = fields.Char("Book Type" , required=True)
     property_ids = fields.One2many("bookstore.book" , "book_type_id" , string="Types")