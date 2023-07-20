from odoo import fields, models

class BookTag(models.Model):

    _name =  "bookstore.tag"
    _description = "Tags of Books"

    name = fields.Char("Name", required=True)
    color = fields.Integer("Color")
