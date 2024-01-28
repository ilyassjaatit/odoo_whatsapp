from odoo import fields, models, _


class WhatsappTemplateReset(models.TransientModel):
    _name = 'whatsapp.template.reset'
    _description = 'Whatsapp Template Reset'

    template_ids = fields.Many2many('whatsapp.template')

    def reset_template(self):
        if not self.template_ids:
            return False
        self.template_ids.reset_template()
        if self.env.context.get('params', {}).get('view_type') == 'list':
            next_action = {'type': 'ir.actions.client', 'tag': 'reload'}
        else:
            next_action = {'type': 'ir.actions.act_window_close'}
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'success',
                'message': _('Whatsapp Templates have been reset'),
                'next': next_action,
            }
        }
