from odoo import models, fields

class PublishBook(models.Model):

    _name = "bookstore.publish"
    _description = "Publish the book"
    

    #name = fields.Char("Publisher", required=True)
    name = fields.Many2one("res.partner", string="Publisher", required= True)
    publish_date = fields.Date("Publish Date", copy=False)
    country = fields.Char("Country of origin")
    book_ids = fields.One2many("bookstore.book", "publish_id", string="Books")

    