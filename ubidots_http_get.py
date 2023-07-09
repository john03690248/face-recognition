'''
This Example sends harcoded data to Ubidots using the requests
library.

Please install the library using pip install requests

Made by Jose García @https://github.com/jotathebest/
'''

import requests
import time
import sys

'''
global variables
'''

ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "database"
VARIABLE_LABEL = ["Ben", "Johnson", "Niezan"]
TOKEN = "BBFF-slbNPRtue9UXuRoNUWwbYbTLcsMPIh" # replace with your TOKEN
DELAY = 1  # Delay in seconds


# def get_var(url=ENDPOINT, device=DEVICE_LABEL, variable="Ben",
#             token=TOKEN):
#     accounts = list()
#     passwords = list()
#     gamils = list()
#     length = len(VARIABLE_LABEL)
#     try:
#         url = "http://{}/api/v1.6/devices/{}/{}/values".format(url,
#                                                         device,
#                                                         variable)
#         headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

#         attempts = 0
#         status_code = 400
#         value1 = ""
#         value2 = ""
#         value3 = ""
#         while status_code >= 400 and attempts < 1:
#             print("[INFO] Retrieving data, attempt number: {}".format(attempts))
#             #payload = {"account": 'value1', "password": 'value2', "gmail": 'value3'}
#             req = requests.get(url=url, headers = headers)
#             status_code = req.status_code
#             attempts += 1
        #     time.sleep(1)

        # print("[INFO] Results:")
#         #print(req.text)
#         #print(req.json()['results'][0]['context']['account'])
#     except Exception as e:
#         print("[ERROR] Error posting, details: {}".format(e))

def get_vars(url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
    try:
        #url = "http://{}/api/v1.6/devices/{}/variables".format(url,device)
        url = "http://industrial.api.ubidots.com/api/v1.6/datasources/63c40d3b45d2af000d956838/variables"
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400
        while status_code >= 400 and attempts < 1:
            #print("[INFO] Retrieving data, attempt number: {}".format(attempts))
            req = requests.get(url=url, headers = headers)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        # print("[INFO] Results:")
        # print(req.json()['count']) #幾個人
        # print(req.json()['results'][0]['name']) #第幾個人的名字
        # print(req.json()['results'][0]['last_value']['context']['account']) #第幾個人的資料
        return req.json()
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

# if __name__ == "__main__":
#     if TOKEN == "...":
#         print("Error: replace the TOKEN string with your API Credentials.")
#         sys.exit()
#     #while True:
#     #get_var()
#     get_vars()
#     time.sleep(DELAY)
