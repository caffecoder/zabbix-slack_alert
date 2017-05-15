#!/usr/bin/env python

import requests
import sys

slack_user_name = 'zabbix'

slack_webhook_url = 'https://hooks.slack.com/services/rest_of_your_webhook_url_part'

result = 1

if len(sys.argv) != 3:
    print('Usage:')
    print(' - zabbix-slack_alert.py "#channel_name" "message"')
    print(' - zabbix-slack_alert.py "@user_name" "message"')

    sys.exit(result)

alert_data = {
    'channel': "%s" % sys.argv[1],
    'username': slack_user_name,
    'text': "%s" % sys.argv[2],
}

headers_data = { 'User-Agent': 'ZABBIX Alert Script (see: https://github.com/xcdr/zabbix-slack_alert)' }

requests.packages.urllib3.disable_warnings()
response = requests.post(slack_webhook_url, headers=headers_data, json=alert_data)

if response.status_code == 200:
    result = 0

sys.exit(result)
