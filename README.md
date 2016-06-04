# Description

Simple script for sending alerts to slack channel from ZABBIX.

## Install required python packages

```shell
root@zabbix-host# pip install requests
```

or

```shell
root@zabbix-host# apt-get install python-requests
```

## Initial config

An incoming Webhook integration must be created within your slack.com account which can be done at https://my.slack.com/services/new/incoming-webhook.

If You already have Webhook, then simply update 'slack_user_name' and 'slack_webhook_url' variables in `zabbix-slack_alert.py`.

## Install at zabbix server

```shell
root@zabbix-host# grep AlertScriptsPath /etc/zabbix/zabbix_server.conf
AlertScriptsPath=/etc/zabbix/alert.d/

root@zabbix-host# cp zabbix-slack_alert.py /etc/zabbix/alert.d/
root@zabbix-host# chown zabbix:zabbix /etc/zabbix/alert.d/zabbix-slack_alert.py
root@zabbix-host# chmod 700 /etc/zabbix/alert.d/zabbix-slack_alert.py
```

### Simple tests

```shell
root@zabbix-host# ./zabbix-slack_alert.py "#your_slack_channel" "Test message to channel."
root@zabbix-host# ./zabbix-slack_alert.py "@your_slack_user" "Test message to user."
```

## Zabbix web interface example

At Administration / Media types / Create Media Type:
- Name: Slack
- Type: Script
- Script name: zabbix-slack_alert.py

At Administration / Users / Admin / Media / Add:
- Type: Slack
- Send to: @your_slack_user
- Script parameters: {ALERT.SENDTO} {ALERT.SUBJECT}

You can also create user 'Slack', next create media with send to #your_slack_channel and assign this user to group Administrators.

After these steps, usage of this media type is the same as others.

## License

This project is released under the [MIT License](http://www.opensource.org/licenses/MIT).

## Additional information

Tested on Debian Jessie with Zabbix 3.0 packages.

- [Zabbix Documentation](https://www.zabbix.com/documentation/3.0/manual/config/notifications/media/script)
- [Slack API](https://api.slack.com/incoming-webhooks#sending_messages)
