from flask import Blueprint,request
from app.main.service.messagging_service import client,answer,bot_number,create_image
import re


Controller_blueprint = Blueprint("QAController_blueprint", __name__)

@Controller_blueprint.route('/', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    whatsapp_number = request.form.get('From')

    if re.search("^image:*", message):
        client.messages \
            .create(
            media_url=create_image(message),
            from_=bot_number,
            to=whatsapp_number
        )
    else:
        client.messages \
            .create(
            body=answer(message),
            from_=bot_number,
            to=whatsapp_number
        )

    return "ok"

