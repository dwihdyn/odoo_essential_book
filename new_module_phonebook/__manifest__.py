
{
    'name': 'New Module',
    'description': 'Inheriting model and odoo view',
    'author': 'Dwi',
    'depends': ['base','sale'],
    'application': True,
    
    'summary': 'Inheriting model and odoo view',
    'version': '0.1',
    'license': 'LGPL-3',
    'website': 'partsindo.co.id',
    'category': 'Sale',

    'data' : [
        'views/views.xml',
        'views/phonebook_view.xml',
    ],

    # 'demo' : [
    #     'demo/demo.xml',
    # ],
}