from __future__ import print_function

from slackbot.bot import listen_to
from slackbot import settings

def format_msg(ticket_id, data):
    if data is None:
        print("Failed to fetch info for #%s" % ticket_id)
        return
    
    if "ticket" not in data:
        print("Unknown ticket #%s" % ticket_id)
        return
    
    msg = "<https://%s.zendesk.com/agent/tickets/%s|#%s: %s>\n" % (
        settings.ZENDESK_APP,
        ticket_id,
        ticket_id,
        data["ticket"]["subject"]
        )
    msg += "*Created*: %s\n" % data["ticket"]["created_at"]
    msg += "*Priority*: %s\n" % data["ticket"]["priority"]
    msg += "*Status*: %s" % data["ticket"]["status"]
    
    return msg

@listen_to('#(\d+)')
@listen_to('ZD-(\d+)')
@listen_to('https:\/\/%s\.zendesk\.com\/agent\/tickets\/(\d+)' % settings.ZENDESK_APP)
def response_ticket_id(message, ticket_id=None):
    try:
        print("processing %s..." % ticket_id)
        data = settings.zendesk_class.get_ticket(ticket_id)
    except Exception as e:
        print(e)
        data = None
        
    msg = format_msg(ticket_id, data)
    if msg is None:
        return
    
    message.send_webapi(msg)
