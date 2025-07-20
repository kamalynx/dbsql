import logging

import telegram
from asgiref.sync import async_to_sync
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site


logger = logging.getLogger(__name__)


@async_to_sync
async def send_message_to_tg_channel(
    message: str,
    token: str,
    # ~ screenshot_path: str,
    chat_id: str
) -> None:
    bot = telegram.Bot(token=token)
    await bot.send_message(
        chat_id=chat_id,
        # ~ photo=screenshot_path,
        text=message,
        parse_mode='HTML',
    )
