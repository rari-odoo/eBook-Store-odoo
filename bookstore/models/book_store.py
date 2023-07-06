from odoo import models, fields

class Book(models.Model):
    _name = "bookstore.book"
    _description = "Book Store Application"
    _log_access = False


    name = fields.Char("Book Title", required=True)
    expceted_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly = False)
    year = fields.Date("Year", required = True )
    description  = fields.Text("Description")
    isbn_code = fields.Integer("ISBN code")
    author_id = fields.Many2one("bookstore.author", string="Author" )
    book_type_id = fields.Many2one("bookstore.book.type","book_ids")