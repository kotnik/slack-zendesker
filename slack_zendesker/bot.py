from __future__ import print_function

from slackbot.bot import listen_to
from slackbot import settings

def format_msg(ticket_id, data):
    if data:
        if data.get("ticket"):
            msg = '<https://%s.zendesk.com/agent/tickets/%s|#%s: %s>\n' % (
                settings.ZENDESK_APP,
                ticket_id,
                ticket_id,
                data["ticket"]["subject"]
                )
            msg += '*Created*: %s\n' % data["ticket"]["created_at"]
            msg += '*Priority*: %s\n' % data["ticket"]["priority"]
            msg += '*Status*: %s' % data["ticket"]["status"]
        else:
            msg = 'Unknown ticket #%s' % ticket_id
    else:
        msg = 'Failed to fetch info for #%s' % ticket_id
    return msg

@listen_to(r'\b(?<=#)(\d+)\b')
@listen_to('https:\/\/(.*)\.zendesk\.com\/agent\/tickets\/(\d+)')
def response_ticket_id(message, app=None, ticket_id=None):
    if ticket_id is None:
        ticket_id = app
    elif app != settings.ZENDESK_APP:
        print("skipping beacuse %s is not our app" % app)
        return

    try:
        print("processing %s..." % ticket_id)
        data = settings.zendesk_class.get_ticket(ticket_id)
    except Exception as e:
        print(e)
        data = None
    message.send_webapi(format_msg(ticket_id, data))
