from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ServerActions(models.Model):
    """ Add Whatsapp option in server actions. """
    _name = 'ir.actions.server'
    _inherit = ['ir.actions.server']

    state = fields.Selection(selection_add=[
        ('whatsapp', 'Send Whatsapp Message'),
    ], ondelete={'whatsapp': 'cascade'})
    # whatsapp
    whatsapp_template_id = fields.Many2one(
        'whatsapp.template', '"hatsapp Template',
        compute='_compute_whatsapp_template_id',
        ondelete='set null', readonly=False, store=True,
        domain="[('model_id', '=', model_id)]",
    )
    whatsapp_method = fields.Selection(
        selection=[('whatsapp', 'Whatsapp'), ('comment', 'Post as Message'), ('note', 'Post as Note')],
        string='Send as (Whatsapp)',
        compute='_compute_whatsapp_method',
        readonly=False, store=True,
        help='Choose method for Whatsapp sending:\nWhatsapp: mass Whatsapp\nPost as Message: log on document\nPost as Note: mass Whatsapp with archives')

    @api.depends('model_id', 'state')
    def _compute_whatsapp_template_id(self):
        to_reset = self.filtered(
            lambda act: act.state != 'whatsapp' or \
                        (act.model_id != act.whatsapp_template_id.model_id)
        )
        if to_reset:
            to_reset.whatsapp_template_id = False

    @api.depends('state')
    def _compute_whatsapp_method(self):
        to_reset = self.filtered(lambda act: act.state != 'whatsapp')
        if to_reset:
            to_reset.whatsapp_method = False
        other = self - to_reset
        if other:
            other.whatsapp_method = 'whatsapp'

    def _check_model_coherency(self):
        super()._check_model_coherency()
        for action in self:
            if action.state == 'whatsapp' and (action.model_id.transient or not action.model_id.is_mail_thread):
                raise ValidationError(_("Sending Whatsapp can only be done on a mail.thread or a transient model"))

    def _run_action_whatsapp_multi(self, eval_context=None):
        # TDE CLEANME: when going to new api with server action, remove action
        if not self.whatsapp_template_id or self._is_recompute():
            return False

        records = eval_context.get('records') or eval_context.get('record')
        if not records:
            return False

        composer = self.env['whatsapp.composer'].with_context(
            default_res_model=records._name,
            default_res_ids=records.ids,
            default_composition_mode='comment' if self.whatsapp_method == 'comment' else 'mass',
            default_template_id=self.whatsapp_template_id.id,
            default_mass_keep_log=self.whatsapp_method == 'note',
        ).create({})
        composer.action_send_whatsapp()
        return False
