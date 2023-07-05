{
    'name' : 'Book Store',
    'summary': "Book Store App",
    'author': "Odoo",

    'depends' : ['base','web'],
    'application': True,
    'installable':True,

    'data' : [
       'security/ir.model.access.csv',
       'views/book_view.xml',
       'views/book_menus.xml'
    ]
}