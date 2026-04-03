import time
import ansible_runner

try:
    import requests
    has_requests = True
except ImportError:
    import urllib.request
    import urllib.error
    has_requests = False

# Monitoring Script
URL = "http://127.0.0.1:5000"


def check_service():
    try:
        if has_requests:
            response = requests.get(URL, timeout=2)
            status = response.status_code
        else:
            req = urllib.request.Request(URL)
            with urllib.request.urlopen(req, timeout=2) as resp:
                status = resp.getcode()

        if status == 200:
            print("IS UP")
        else:
            print("NOT UP")
    except Exception:
        print("Service Error")
        status = None
    return status


while True:
    status = check_service()
    if status is None or status != 200:
        ansible_runner.run(private_data_dir='Brain/project/', playbook='restart_container.yaml')
    time.sleep(5)

# Adding an Offline LLM 
