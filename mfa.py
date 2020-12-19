import requests
from datetime import date
from datetime import datetime
from datetime import timedelta

from slack import WebClient
from slack.errors import SlackApiError

def addzero(num):
    return (str(num) if len(str(num)) == 2 else '0' + str(num))

slack_token = ''
slack_channel = ''
query = 'https://online.mfa.gov.ua/api/v1/queue/consulates/30/schedule?date={}&dateEnd={}&serviceId=181'

today_str = str(date.today().year) + '-' + addzero(date.today().month) + '-' + addzero(date.today().day)
future = date.today() + timedelta(days=30)
future_str = str(future.year) + '-' + addzero(future.month) + '-' + addzero(future.day)
msg = ''

try:
    r = requests.get(query.format(today_str, future_str), allow_redirects=True)
    msg = str(r.json())
except Exception as e:
    msg = 'Something went wrong: ' + str(e)
    pass

if "from" in msg:
    client = WebClient(token=slack_token)
    response = client.chat_postMessage(channel=slack_channel, text='There are available slots\n\n' + msg, as_user='true')
