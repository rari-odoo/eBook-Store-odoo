from odoo import fields, models

class BookPolicy(models.Model):
    _name = "bookstore.policy"
    _description = "Book Pocily & configuration"
    _rec_name = "policy_name"
    _log_access = False

    policy_name = fields.Char("Policy",required=True)
    policy_days = fields.Integer("Day(s) to keep the book")
    fine = fields.Integer("Fine", required=True) 