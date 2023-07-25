from odoo import models, fields

class PublishBook(models.Model):

    _name = "bookstore.publish"
    _description = "Publish the book"
    

    name = fields.Char("Publisher", required=True)
    #name = fields.One2many("res.partner", string="Publisher", required= True)
    publish_date = fields.Date("Publish Date", copy=False)
    country = fields.Selection([('i','India'),('am','America'),('c',"China"),('Af','Africa'),('cn','Canada'),('au','Australia'),('g',"German"),('ag','Afghanistan'),('f','France'),('b','Bagladesh'),('p','Nepal'),('pl','Philippines'),('bt',"Bhutan"),('l','Shir Lanka')],"Country of origin")
    book_ids = fields.One2many("bookstore.book", "publish_id", string="Books")

    # _sql_constraints = [
    #     ('unique publisher', 'UNIQUE(name)', 'Publisher should be unique')
    # ]