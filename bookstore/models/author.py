from odoo import models, fields

class authorBook(models.Model):
    _inherit = "res.partner"
    _description = "Author Details"

    book_ids = fields.One2many("bookstore.book", 'author_id', string="Author")
    # book_ids = fields.Many2many("bookstore.book",)