# API_Request
# Quick Python script used to send request via REST API
# For testing purposes with the web server
# (c) 2021 Richard Jouas

import requests
from requests.structures import CaseInsensitiveDict

url = "http://127.0.0.1:8000/api/temperature/"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Token "
headers["Content-Type"] = "application/json"

data = """
{
	"temp": 12.5
}
"""

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
