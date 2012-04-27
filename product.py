# -*- encoding: utf-8 -*-

import netsvc
import pooler, tools
import math

from tools.translate import _

from osv import fields, osv

class product_product(osv.osv):
    
    _inherit = 'product.product'
    
    _columns = {'abilita_mod':fields.selection([
                    ('si','Modifica abilitata'),
                    ('no','Modifica Non abilitata'),
                    ],    'Abilita Modifica del Prezzo', select=True),
                }
    
    _defaults = { 'abilita_mod' : lambda * a:'no'}
    
    
product_product()