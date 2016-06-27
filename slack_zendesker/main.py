from __future__ import print_function

import sys

from slackbot import settings
settings.PLUGINS = [
    'slack_zendesker.bot',
]
from slackbot.bot import Bot


def main():
    try:
        settings.ZENDESK_URL
    except AttributeError:
        print('Missing SLACKBOT_ZENDESK_URL environment variable')
        sys.exit(1)

    bot = Bot()
    bot.run()
