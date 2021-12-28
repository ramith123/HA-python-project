# HA-python-project

This is a personal project that uses the [Home Assistant api]( https://www.home-assistant.io/) and a little bit of python to create a custom CLI to control lights, ac etc...

not really useful out of the box but someone could find a use for it..

the `.CustomHA` folder should be located in your home folder (User folder on windows) and the `secret.json` should has a token and the url of your HA

names of the lights and ac can be changed from `data.json` file.

To install on linux:

1. Clone this repo to somewhere `git clone https://github.com/ramith123/HA-python-project.git`
1. `pip install HA-python-project/`
1. Copy `.CustomHA` folder home folder `cp HA-python-project/.CustomHA -r ~`
1. change values in data and secrect json files

More or exactly the same thing for windows. Have pip and copy the .CustomHA folder to the user folder.

On Home assitant side, generate a token [Follow the thread if needed](https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159/2). Add this to `secrect.json` file along with the url.

Currently this program can control an (1) ac and multiple lights. 

You can control the ac by typing to the command line:

`bac on` to turn on ac

`bac off` to turn off ac

`bac <num>` to set temperature of ac

You can control lights by:

`blight <light> <on|off>`
`blight <light> <num>` to set brightness
`blight all <same as above>` apply effects for all lights.

if a command is successful, it should print out the json data returned by the api.
