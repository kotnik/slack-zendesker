import requests
import multiprocessing


class Zendesk(object):
    def __init__(self, zendesk_url, user, password, timeout=5.0):
        self.zendesk_url = zendesk_url
        self.auth = (user, password)
        self.timeout = timeout

    def _query(self, url):
        return requests.get(url, auth=self.auth)

    def get_ticket(self, ticket_id):
        url = '%s/api/v2/tickets/%s.json' % (self.zendesk_url, ticket_id)

        pool = multiprocessing.Pool(1)
        query = pool.map_async(self._query, [url])
        try:
            result = query.get(timeout=self.timeout)
        except multiprocessing.context.TimeoutError:
            return None

        pool.terminate()

        if result and len(result) > 0:
            return result[0].json()
        return None
