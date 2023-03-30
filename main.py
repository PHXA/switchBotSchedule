import requests
import json
from dotenv import load_dotenv
import os
import datetime
import numpy as np
import time

load_dotenv()

TOKEN = os.environ["TOKEN"]
API_HOST = os.environ["API_HOST"]
DEBIVELIST_URL = f"{API_HOST}/v1.0/devices"
DEVICE_ID = os.environ["DEVICE_ID"]

HEADERS = {
  'Authorization': TOKEN,
  'Content-Type': 'application/json; charset=utf8'
}

def _get_request(url):
  res = requests.get(url, headers=HEADERS)
  data = res.json()
  if data['message'] == 'success':
      return res.json()
  return {}

def _post_request(url, params):
  res = requests.post(url, data=json.dumps(params), headers=HEADERS) 
  data = res.json()
  if data['message'] == 'success':
      return res.json()
  return {}

def get_device_list():
  try:
    a=_get_request(DEBIVELIST_URL)["body"]['deviceList']
    print(a)
    return a
  except:
    return

def send_button(deviceId=DEVICE_ID,):
  url = f"{API_HOST}/v1.0/devices/{deviceId}/commands"
  params = {
      "command": "turnOn",
      "parameter": "default",
      "commandType": "command"
  }
  res = _post_request(url, params)
  if res['message'] == 'success':
      return res
  return {}

schedule=[0,2,4,6,8,10,12,14,16,18,20,22] # 時間を指定
schedule=sorted(schedule)
schedule=np.array(schedule)
def run():
  while 1:
    now = datetime.datetime.now()
    next = now
    future_is=schedule[schedule>now.hour]
    if sum(future_is)==0:
      next=datetime.timedelta(days=1)+next
      next=next.replace(hour=schedule[0],minute=0,second=0,microsecond=0)
    else:
      next=next.replace(hour=future_is[0],minute=0,second=0,microsecond=0)
    send_button()
    s=now.timestamp()
    e=next.timestamp()
    print(f"now: {now}, next: {next}, sleep: {(e-s)/60} [min]")
    time.sleep(e-s)
   
if "__main__" == __name__:
  # data = get_device_list()
  run()
