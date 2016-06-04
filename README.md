## Description:

Simple script for sending alerts to slack channel from ZABBIX.

## Install required python packages:

```shell
pip install requests
```

## Config:

Simply update 'slack_user_name' and 'slack_webhook_url' variables in `zabbix-slack_alert.py`.

## Test of usage:

```shell
./zabbix-slack_alert.py your_slack_channel "Test message."
```
