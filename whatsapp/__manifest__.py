{
    "name": "Whatsapp gateway",
    "version": "0.0.1",
    "category": "Hidden/Tools",
    "summary": "Whatsapp Text Messaging",
    "description": """This module gives a framework for Whatsapp text messaging----------------------------------------------------""",
    "depends": ["base", "iap_mail", "mail", "phone_validation"],
    "data": [
        "security/ir.model.access.csv",
        "views/whatsapp_whatsapp_views.xml",
        "wizard/whatsapp_template_reset_views.xml",
        "wizard/whatsapp_template_preview_views.xml",
        "wizard/whatsapp_composer_views.xml",
        "views/whatsapp_template_views.xml",
    ],
    
    "demo": [],
    "installable": True,
    "auto_install": True,
    "assets": {},
    "license": "LGPL-3",
}
