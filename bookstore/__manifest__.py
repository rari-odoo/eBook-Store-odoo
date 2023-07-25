{
    'name' : 'Book Store',
    'summary': "Book Store App",
    'author': "Odoo",

    'depends' : ['base','web','mail'],
    'application': True,
    'installable':True,

    'data' : [
       'security/ir.model.access.csv',
       'views/book_stock_view.xml'
       'views/book_policy_view.xml',
       'views/publish_view.xml',
       'views/author_view.xml',
       'views/book_view.xml',
       'views/book_type_view.xml',
       'views/book_menus.xml',
    ],

    'demo' : [
         'demo/demo_data.xml',
    ]
}