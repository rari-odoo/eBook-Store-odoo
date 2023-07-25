from odoo import models, fields

class BookStock(models.Model):
    _name = "bookstore.bookstock"
    _description = "Book Stock"

    quantity = fields.Integer("Quantity of Book")
    