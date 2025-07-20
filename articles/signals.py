from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site
from django.conf import settings
from django.template.loader import render_to_string

from articles.models import Article
from articles.bot import send_message_to_tg_channel


@receiver(post_save, sender=Article)
def send_tg_message(sender, instance, created, **kwargs):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    if all([created, token, chat_id, instance.is_published]):
        site = Site.objects.get_current().domain
        message = render_to_string(
            'tg_message.html', context={'article': instance, 'site': site}
        )
        send_message_to_tg_channel(
            message=message,
            token=token,
            chat_id=chat_id,
            # ~ screenshot_path=instance.image.path,
        )
