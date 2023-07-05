from odoo import models, fields

class Book(models.Model):
    _name = "bookstore.book"
    _description = "Book Store Application"
    _log_access = False


    name = fields.Char("Book Title", required=True)
    Expceted_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly = False)
    year = fields.Integer("Year", required = True)
    description  = fields.Text("Description")
    isbn_code = fields.Integer("ISBN code")
    author_ids = fields.Many2many("bookstore.author", "full_name", "Author" )
    book_type_id = fields.Many2one("bookstore.book.type", string="Book Type")