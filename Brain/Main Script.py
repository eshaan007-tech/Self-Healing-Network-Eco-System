import requests
import time
import urllib 

# For Checking if the given server is UP/DOWN or ERROR 

URL = "http://127.0.0.1:5000"

while True:
    try:
        response= requests.get(URL , timeout=2)
        if  response.status_code==200:
            print("IS UP")
        else :
            print("NOT UP")
    except:
        print ("Service Error")
time.sleep(5)


