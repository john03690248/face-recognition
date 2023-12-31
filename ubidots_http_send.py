'''
This Example sends harcoded data to Ubidots using the request HTTP
library.

Please install the library using pip install requests

Made by Jose García @https://github.com/jotathebest/
'''

import requests
import random
import time
import sys

'''
global variables
'''

ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "database"
VARIABLE_LABEL1 = "Johnson"
VARIABLE_LABEL2 = "Ben"
VARIABLE_LABEL3 = "Niezan"
TOKEN = "xxxx" # replace with your TOKEN
DELAY = 1  # Delay in seconds


def post_var(payload, url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}".format(url, device)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 1:
            #print("[INFO] Sending data, attempt number: {}".format(attempts))
            req = requests.post(url=url, headers=headers,
                                json=payload)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        #print("[INFO] Results:")
        #print(req.text)
        #print(payload)
        #print("-------------------------------")
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

def send(add_variable, account, password, gmail):
    # Simulates name values
    # Builds Payload and topíc
    payload = {add_variable: {"value" : 0, "context":{"account" : account, "password" : password, "gmail" : gmail}}}
    # Sends data
    post_var(payload)
    
    # # Simulates name values
    # account = "xxx"
    # password = "xxx"
    # gmail = "xxx"
    # # Builds Payload and topíc
    # payload = {VARIABLE_LABEL2: {"value" : 7, "context":{"account" : account, "password" : password, "gmail" : gmail}}}
    # # Sends data
    # post_var(payload)

# if __name__ == "__main__":
#     if TOKEN == "...":
#         print("Error: replace the TOKEN string with your API Credentials.")
#         sys.exit()
#     #while True:
#     main()
#     time.sleep(DELAY)
