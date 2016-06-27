# Slack zendersker

Expands `#\d+` to Zendesk URLs for lazyness reasons.

To install:

```
mkdir slack-zendesker
cd slack-zendesker
virtualenv .env/
pip install -e git+git@github.com:kotnik/slack-zendesker.git#egg=slack_zendesker
```

To run:

```
export SLACKBOT_API_TOKEN=YOUR_BOT_API_TOKEN
export SLACKBOT_ZENDESK_URL=https://YOURAPP.zendesk.com
slack_zendesker
```
