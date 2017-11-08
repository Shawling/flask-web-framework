import requests
import json
import time

domain = 'http://127.0.0.1:9000/'

url = 'api/detecteHistory'
# pin_list = [35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
# para = {
#     'mac_addr': 'aabbccddeeff',
#     'pin_list': json.dumps(pin_list)
# }

para = {
    'mac_addr': 'aabbccddeeff',
    'time_from': time.mktime(time.strptime('2017-11-08 00:00:00', '%Y-%m-%d %H:%M:%S')),
    'time_to': time.mktime(time.strptime('2017-11-09 00:00:00', '%Y-%m-%d %H:%M:%S'))
}

response = requests.get(domain + url, params=para)
if not response.status_code == 200:
    print(response.text)
else:
    print(response.json())