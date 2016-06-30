from __future__ import print_function

import sys

from slackbot import settings
settings.PLUGINS = [
    'slack_zendesker.bot',
]
from slackbot.bot import Bot

from .zendesk import Zendesk

def main():
    try:
        settings.ZENDESK_URL
        settings.ZENDESK_USER
        settings.ZENDESK_PASS
    except AttributeError:
        print('Missing SLACKBOT_ZENDESK_URL, SLACKBOT_ZENDESK_USER or SLACKBOT_ZENDESK_PASS environment variable')
        sys.exit(1)

    settings.zendesk_class = Zendesk(
        settings.ZENDESK_URL,
        settings.ZENDESK_USER,
        settings.ZENDESK_PASS,
    )

    print("starting bot...")
    bot = Bot()
    bot.run()
