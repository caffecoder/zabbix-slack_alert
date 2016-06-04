#!/usr/bin/env python

# Requirements:
# pip install requests

import requests
import sys

slack_user_name = 'alert-bot'
slack_webhook_url = 'https://hooks.slack.com/services/rest_of_your_webhook_url_part'

if len(sys.argv) != 3:
    print('Usage: alert-bot.py channel_name "message"')
    sys.exit(1)

alert_data = {
    "channel": "#%s" % sys.argv[1],
    "username": slack_user_name,
    "text": "%s" % sys.argv[2],
}

requests.packages.urllib3.disable_warnings()
response = requests.post(slack_webhook_url, json=alert_data)

result = 0 if response.status_code == 200 else 1

sys.exit(result)
