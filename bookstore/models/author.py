from odoo import models, fields, api

class Book(models.Model):
    _name = "bookstore.author"
    _description = "Author Details"
    _log_access = False

    # first_name = fields.Char("First Name", required= True)
    # last_name = fields.Char("Last Name", required= True)
    name = fields.Char("Author Name" , required=True)
    author_ids = fields.One2many("bookstore.book" , "author_id")
   # book_ids = fields.Many2many()
    #author_ids = fields.Many2many("bookstore.book", "author_id", string="Author")


    # @api.depends('first_name','last_name')
    # def _compute_full_name(self):
    #     for i in self:
    #       i.full_name = str(i.first_name) + ' ' + str(i.last_name)
    #       #print(type(i.full_name))