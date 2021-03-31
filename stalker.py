import os

print("init...")
os.system("pip3 install requests")
os.system("pip3 install colorama")
import requests
from colorama import Fore
from datetime import datetime
import os
import time
import json

try:
    os.mkdir("./logs")
except:
    print()


def getjson(url, data=None):
    response = requests.get(url, params=data)
    return json.loads(response.text)


class User:
    def __init__(self, id, status, online):
        self.id = id
        self.status = status
        self.online = online


print(Fore.BLUE)
print(
    " ▄▀▀▄ ▄▀▀▄  ▄▀▀▄ █      ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄   ▄▀▀▀▀▄      ▄▀▀▄ █  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ "
)
print(
    "█   █    █ █  █ ▄▀     █ █   ▐ █    █  ▐ ▐ ▄▀ ▀▄ █    █      █  █ ▄▀ ▐  ▄▀   ▐ █   █   █ "
)
print(
    "▐  █    █  ▐  █▀▄         ▀▄   ▐   █       █▄▄▄█ ▐    █      ▐  █▀▄    █▄▄▄▄▄  ▐  █▀▀█▀  "
)
print(
    "   █   ▄▀    █   █     ▀▄   █     █       ▄▀   █     █         █   █   █    ▌   ▄▀    █  "
)
print(
    "    ▀▄▀    ▄▀   █       █▀▀▀    ▄▀       █   ▄▀    ▄█▄▄▄▄▄▄▀ ▄▀   █   ▄█▄▄▄▄   █     █   "
)
token = input(
    "\ntoken (https://oauth.vk.com/authorize?client_id=7757764&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.130&scope=conversations):\n"
)

ids = input("user(s) id (comma separated):\n")

idsArray = ids.split(",")

delay = float(input("delay (seconds): "))

file1 = open(
    "./logs/" + datetime.now().strftime("%d%m%Y%H%M%S") + ".txt", "w+", encoding="utf-8"
)
users = []


for id in idsArray:
    users.append(User(id, "", 0))


file1.write(
    "starting stalker with arguments:\ntoken: "
    + token
    + "\nids: "
    + ids
    + "\ndelay: "
    + str(delay)
    + "\n\n"
)
print(
    "\nstarting stalker with arguments:\ntoken: "
    + token
    + "\nids: "
    + ids
    + "\ndelay: "
    + str(delay)
    + "\n"
)

while True:
    for userr in users:
        userGet = getjson(
            "https://api.vk.com/method/users.get?v=5.130&access_token="
            + token
            + "&user_id="
            + userr.id
            + "&fields=online,status"
        )
        user = userGet["response"][0]
        if userr.status != user["status"]:
            print(
                "["
                + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                + "] "
                + user["first_name"]
                + " "
                + user["last_name"]
                + ' changed status: "'
                + userr.status
                + '" => "'
                + user["status"]
                + '"'
            )
            file1.write(
                "["
                + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                + "] "
                + user["first_name"]
                + " "
                + user["last_name"]
                + ' changed status: "'
                + userr.status
                + '" => "'
                + user["status"]
                + '"\n'
            )
            userr.status = user["status"]
        if userr.online != user["online"]:
            print(
                "["
                + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                + "] "
                + user["first_name"]
                + " "
                + user["last_name"]
                + ' online change: "'
                + str(userr.online)
                + '" => "'
                + str(user["online"])
                + '"'
            )
            file1.write(
                "["
                + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                + "] "
                + user["first_name"]
                + " "
                + user["last_name"]
                + ' online change: "'
                + str(userr.online)
                + '" => "'
                + str(user["online"])
                + '"\n'
            )
            userr.online = user["online"]
    time.sleep(delay)
