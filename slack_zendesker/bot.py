from slackbot.bot import listen_to
from slackbot import settings


@listen_to('#(\d+)')
def giveme(message, something):
    message.send('Let me expand that Zendesk ticket for you: {}/agent/tickets/{}'.format(settings.ZENDESK_URL, something))
