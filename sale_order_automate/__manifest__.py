# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Order Automation',
    'version' : '16.0',
    'license': 'LGPL-3',
    'category': 'Sales',
    'summary': 'This module allow to make automatic invoice and inventory valiation one confirm sales order.',
    'author':'Samah Kandil',
    'category': 'Sales',
    'summary': """Enable auto sale workflow with sale order confirmation. Include operations like Auto Create Invoice, Auto Validate Invoice and Auto Transfer Delivery Order.""",
    'description': """

        You can directly create invoice and set done to delivery order by single click

    """,
    'website': 'https://www.linkedin.com/in/samah-kandil-odoo',
    'support': 'samahqandeel22@gmail.com',
    'images': ['static/description/imag1.png'],
    'depends' : ['sale_stock'],
    'data': [
        'views/stock_warehouse.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,

}
