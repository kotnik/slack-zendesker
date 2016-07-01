from __future__ import print_function

from slackbot.bot import listen_to
from slackbot import settings


@listen_to('#(\d+)')
def response_ticket_id(message, ticket_id):
    print("processing %s..." % ticket_id)
    try:
        data = settings.zendesk_class.get_ticket(ticket_id)
    except Exception as e:
        print(e)
        data = None

    if data:
        msg = '<%s/agent/tickets/%s|#%s: %s>\n' % (settings.ZENDESK_URL, ticket_id, ticket_id, data["ticket"]["subject"])
        msg += '*Created*: %s\n' % data["ticket"]["created_at"]
        msg += '*Priority*: %s\n' % data["ticket"]["priority"]
        msg += '*Status*: %s' % data["ticket"]["status"]
    else:
        msg = 'Failed to fetch info for #%s' % ticket_id

    message.send_webapi(msg)
