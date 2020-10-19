from requests import get, post
import json
import click
from pathlib import Path

data = None
secret = None
serviceCall = None
homeFolder = str(Path.home())
with open(homeFolder + "/.CustomHA/data.json", "r") as f:
    data = json.load(f)
with open(homeFolder + "/.CustomHA/secret.json", "r") as f:
    secret = json.load(f)
headers = {
    "Authorization": "Bearer " + secret["LToken"].strip(),
    "content-type": "application/json",
}


def doServiceCall(url, headers, data):
    url += data.pop("actionType")
    if "domain" in data:
        url += "/" + data.pop("domain")
    if "action" in data:
        url += "/" + data.pop("action")

    response = post(url, headers=headers, json=data)
    return response.json()


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


url = getAPIUrl(secret)


@click.command()
@click.argument("ans")
def acControls(ans):

    if ans == "on":
        serviceCall = getServiceCallData(data, "ac", "turnOn")
    if ans == "off":
        serviceCall = getServiceCallData(data, "ac", "turnOff")
    if ans.isnumeric():
        serviceCall = getServiceCallData(data, "ac", "setTemp")
        serviceCall["temperature"] = float(ans)

    if APIExists(url, headers):
        try:
            res = doServiceCall(url, headers, serviceCall)
            print(json.dumps(res, indent=2))
        except:
            print("Major error occurred")


@click.command()
@click.argument("light")
@click.argument("command")
def lightsControls(light, command):

    light = light.lower() + "_light"  # naming convention in data
    if command == "on":
        serviceCall = getServiceCallData(data, light, "turnOn")
    if command == "off":
        serviceCall = getServiceCallData(data, light, "turnOff")
    if command.isnumeric():
        serviceCall = getServiceCallData(data, light, "setBrightness")
        serviceCall["brightness_pct"] = int(command)

    if APIExists(url, headers):
        try:
            res = doServiceCall(url, headers, serviceCall)
            print(json.dumps(res, indent=2))
        except:
            print("Major error occurred")
