from requests import get, post
import json

data = None
secret = None
components = None


def doServiceCall(url, headers, data):
    url += data.pop("actionType") + "/" + data.pop("domain") + "/" + data.pop("action")
    response = post(url, headers=headers, json=data)
    return response.json()


def getServiceCallData(data, component, service):
    componentData = getFirstLevelJsonData(data["components"][component])
    serviceData = getFirstLevelJsonData(
        data["components"][component]["services"][service]
    )
    componentData.update(serviceData)
    return componentData


def getFirstLevelJsonData(jsonData):
    returnData = {}

    for key in jsonData.keys():
        if not isinstance(jsonData[key], dict):

            returnData[key] = jsonData[key]
    return returnData


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

components = data["components"]

serviceCall = getServiceCallData(data, "ac", "setTemp")
url = getAPIUrl(secret)
print(serviceCall)
if APIExists(url):
    res = doServiceCall(url, headers, serviceCall)
