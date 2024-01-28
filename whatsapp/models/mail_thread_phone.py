from odoo import models


class PhoneMixin(models.AbstractModel):
    _inherit = 'mail.thread.phone' 

    def _whatsapp_get_number_fields(self):
        """ Add fields coming from mail.thread.phone implementation. """
        phone_fields = self._phone_get_number_fields()
        whatsapp_fields = super(PhoneMixin, self)._whatsapp_get_number_fields()
        for fname in (f for f in whatsapp_fields if f not in phone_fields):
            phone_fields.append(fname)
        return phone_fields