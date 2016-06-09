# -*- coding: utf-8 -*-
# © 2015-2016 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _


class AccountPaymentLine(models.Model):
    _inherit = 'account.payment.line'
    _description = 'Payment Lines'

    communication_type = fields.Selection(selection_add=[('bvr', 'BVR')])

    def invoice_reference_type2communication_type(self):
        res = super(AccountPaymentLine,
                    self).invoice_reference_type2communication_type()
        res.update({'bvr': 'BVR'})
        return res
