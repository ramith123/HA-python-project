from requests import get, post
import json
import click

data = None
secret = None


def doServiceCall(url, headers, data):
    url += data.pop("actionType")
    if "domain" in data:
        url += "/" + data.pop("domain")
    if "action" in data:
        url += "/" + data.pop("action")

    response = post(url, headers=headers, json=data)
    return response.text


def getServiceCallData(data, component, action):
    componentData = getFirstLevelJsonData(data["components"][component])
    actionData = getFirstLevelJsonData(data["components"][component]["actions"][action])
    componentData.update(actionData)
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


def APIExists(url, headers):
    response = get(url, headers=headers)

    if "API running" in response.json()["message"]:
        return True
    return False


@click.command()
@click.argument("ans")
def set_acTemp(ans):

    with open("./.CustomHA/data.json", "r") as f:
        data = json.load(f)
    with open("./.CustomHA/secret.json", "r") as f:
        secret = json.load(f)
    headers = {
        "Authorization": "Bearer " + secret["LToken"].strip(),
        "content-type": "application/json",
    }
    serviceCall = None
    if ans == "on":
        serviceCall = getServiceCallData(data, "ac", "turnOn")
    if ans == "off":
        serviceCall = getServiceCallData(data, "ac", "turnOff")
    if ans.isnumeric():
        serviceCall = getServiceCallData(data, "ac", "setTemp")
        serviceCall["temperature"] = float(ans)

    url = getAPIUrl(secret)

    if APIExists(url, headers):
        res = doServiceCall(url, headers, serviceCall)
        print(res)


@click.command()
def sample():
    print("Test")
