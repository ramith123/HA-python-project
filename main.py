from requests import get, post
import json

data = None
secret = None
serviceCall = {
    "domain": "climate",
    "service": "set_temperature",
    "entity_id": "climate.ac",
    "temperature": 27,
}


def doServiceCall(url, headers, data):
    url += "services/" + data.pop("domain") + "/" + data.pop("service")
    print(data)
    print(url)
    response = post(url, headers=headers, json=data)
    print(response.json())


def getAPIUrl(data):
    url = data["url"]
    if url.endswith("/"):
        return url + "api/"
    return url + "/api/"


def APIExists(url):
    response = get(url, headers=headers)

    if "API running" in response.json()["message"]:
        return True
    return False


with open("data.json", "r") as f:
    data = json.load(f)
with open("secret.json", "r") as f:
    secret = json.load(f)

headers = {
    "Authorization": "Bearer " + secret["LToken"].strip(),
    "content-type": "application/json",
}


url = getAPIUrl(data)
if APIExists(url):
    doServiceCall(url, headers, serviceCall)
