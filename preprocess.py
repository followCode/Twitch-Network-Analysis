from bs4 import BeautifulSoup
import requests
import json
import re
import time
import os
import pandas as pd
import threading

CLIENT_ID = "bv4l8otdvp5iufa3wjd26xezfdlop2"
ID_URL = "https://api.twitch.tv/kraken/users?login={0}&client_id={1}&api_version=5"
FOLLOW_URL = "https://api.twitch.tv/kraken/channels/{0}/follows?client_id={1}&api_version=5&limit=100&cursor={2}"

PATH = os.path.join(os.path.abspath(os.getcwd()), "prep")

def setup():
    folder = "prep"
    path = os.path.join(os.path.abspath(os.getcwd()), folder)
    
    if not os.path.exists(path):
        os.mkdir(path)
        print("[LOG] Making folder")
    else:
        print("[LOG] Preprocess folder already setup")

def getChannelID(channel_name):
    # Send request to get ID to API

    resp = requests.get(ID_URL.format(channel_name, CLIENT_ID))
    json_data = json.loads(resp.text)
    channel_id = json_data["users"][0]["_id"]

    return channel_id

def getTotalFollowers(channel_id):
    # Get the channel follower count
    
    resp = requests.get(FOLLOW_URL.format(channel_id, CLIENT_ID, ""))
    json_data = json.loads(resp.text)
    follower_count = json_data["_total"]

    return follower_count    

def getChannelFollowers(channel_id):
    # Send api requests recursively to get followers
    cursor = ""
    count = 0
    follower_count = getTotalFollowers(channel_id)

    followers = []

    while count<follower_count:
        resp = None
        start = 60
        while resp==None:
            try:
                resp = requests.get(FOLLOW_URL.format(channel_id, CLIENT_ID, cursor))
            except Exception as ex:
                print("[ERR] Twitch load block for: {0}, waiting: {1} seconds".format(str(channel_id), str(start)))
                print(ex)
                time.sleep(start)
                start+=60
        json_data = json.loads(resp.text)
        try:
            cursor = json_data["_cursor"]
        except:
            cursor = ""
        for follower in json_data["follows"]:
            followers.append(follower["user"]["_id"])
            count+=1
        print("[LOG] Collected {0} followers: {1}".format(str(channel_id),str(count)))
        time.sleep(.5)
    
    return followers

    
def loadData(gameCode):
    f = open(gameCode, "r")
    data = f.read()
    f.close()

    soup = BeautifulSoup(data, 'html.parser')
    channels = soup.find_all('a', {"data-test-selector":"ChannelLink"})

    for channel in channels[:10]:
        channel_name = re.findall(r"\/(\w+)\/",channel.attrs["href"])[0]
        channel_id = -1
        try:
            channel_id = getChannelID(channel_name)
        except Exception as e:
            print("[ERR] Channel: {0} Game: {1}".format(channel_name, gameCode))
            break
        print("{0} - {1}".format(channel_name, channel_id))
        followers = getChannelFollowers(channel_id)

        prepFile = os.path.join(PATH, gameCode)
        mode = "w"
        if os.path.exists(prepFile):
            mode = "a"
        print("[LOG] Collecting data for channel: {0}".format(channel_name))
        with open(prepFile, mode) as gameFile:
            string = ""
            for follower in followers:
                string += "{0} {1}\n".format(follower, channel_id)
            gameFile.write(string)
        
        time.sleep(30)

setup()
df = pd.read_csv("data.csv")
threads = []
noCodes = int(df.shape[0]/4)
print(df["code"][:noCodes])
for gameCode in df["code"][:noCodes]:
    print("[LOG] Collecting data for: {0}".format(gameCode))
    x = threading.Thread(target=loadData, args=(gameCode,))
    threads.append(x)
    x.start()
    time.sleep(60)