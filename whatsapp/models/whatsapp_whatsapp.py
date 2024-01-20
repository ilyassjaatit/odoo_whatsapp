import logging
import threading

from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)


class WhatsappWhatsapp(models.Model):
    _name = "whatsapp.whatsapp"
    _description = "Outgoing Whatsapp"
    _rec_name = "number"
    _order = "id DESC"

    number = fields.Char("Number")
    body = fields.Text()
    partner_id = fields.Many2one("res.partner", "Customer")
    mail_message_id = fields.Many2one("mail.message", index=True)
    state = fields.Selection(
        [
            ("outgoing", "In Queue"),
            ("sent", "Sent"),
            ("error", "Error"),
            ("canceled", "Canceled"),
        ],
        "Whatsapp Status",
        readonly=True,
        copy=False,
        default="outgoing",
        required=True,
    )
    failure_type = fields.Selection([], copy=False)

    def send(self):
        """ Main API method to send Whatsapp.
        """
        raise "method not implemented"

    def action_set_error(self):
        raise "method not implemented"

    def action_set_outgoing(self):
        raise "method not implemented"

    def action_set_canceled(self):
        raise "method not implemented"