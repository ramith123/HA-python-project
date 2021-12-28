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
