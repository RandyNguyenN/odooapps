# -*- coding: utf-8 -*-
#############################################################################
#
#    Odoo Master.
#
#    Copyright (C) 2023-TODAY Odoo Master (<https://www.odoomaster.com>)
#    Author: Odoo Master (<https://www.odoomaster.net>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Simple Scheduled Actions',
    'version': '16.0.1.0.0',
    'summary': """Simple Scheduled Actions""",
    'description': """This Module Scheduled Actions in Odoo allows users to easily define and manage automated functions on a scheduled basis. 
    Instead of performing tasks manually, users can utilize this module to call specific functions and actions at regular intervals or specific times.""",
    'author': 'Odoo Master',
    'company': 'Odoo Master',
    'website': "https://www.odoomaster.net",
    'category': 'Inventory',
    'maintainer': 'Odoo Master',
    'depends': [],
    'data': ['views/ir_cron.xml',],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
