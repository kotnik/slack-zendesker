# Slack zendersker

Expands `#\d+` to Zendesk description for lazyness reasons.

To install:

```
mkdir slack-zendesker
cd slack-zendesker
virtualenv .env/
source .env/bin/activate
pip install -e git+git@github.com:kotnik/slack-zendesker.git#egg=slack_zendesker
```

To run:

```
export SLACKBOT_API_TOKEN=YOUR_BOT_API_TOKEN
export SLACKBOT_ZENDESK_URL=https://YOURAPP.zendesk.com
export SLACKBOT_ZENDESK_USER='your@mail.com/token'
export SLACKBOT_ZENDESK_PASS='TOKEN'
slack_zendesker
```
