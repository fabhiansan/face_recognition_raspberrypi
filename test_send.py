import requests
import logging

import http.client

http.client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

API_ENDPOINT = "http://192.168.1.8:3000/face"

data_post = {
                'face_detected' : "test",
                'emotion' : "Happy"   
            }

x = requests.post(API_ENDPOINT, data = data_post)

print(x.text)