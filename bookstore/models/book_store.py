from odoo import models, fields


class Book(models.Model):
    _name = "bookstore.book"
    _description = "Book Details"
    _inherit = "mail.thread"
    _log_access = False

    name = fields.Char("Book Title", required=True)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=False)
    date = fields.Date("Date", required=True, default=lambda self: fields.Datetime.today())
    description = fields.Text("Description")
    edition = fields.Char("Edition")
    isbn_code = fields.Integer("ISBN code")
    termCon = fields.Text("Terms and Conditions")
    state = fields.Selection([('n', 'New'), ('a', 'Available'),('not', 'Not Available'), ('s', "sold"), ('C', 'Canceled')], default = 'n')
    publish_id = fields.Many2one("bookstore.publish", "Publisher")
    p_not = fields.Selection([('p', 'Publish'), ('un', 'Unpublish')], "Status")
    author_id = fields.Many2one("res.partner", string="Author", required=True)
    author_email = fields.Char(related="author_id.email",string="Email")
    contact_no = fields.Char(related="author_id.phone",string="Contact Number")
    book_type_id = fields.Many2one("bookstore.book.type", string="Book Type")
    #tag_ids = fields.Many2many("bookstore.tag", "Tags")
    sequence = fields.Integer("Sequence", default = 10)

    