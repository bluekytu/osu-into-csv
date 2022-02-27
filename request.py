from contextlib import redirect_stdout
from email import header
import string
from xml.etree.ElementTree import tostring
import requests
import json
import simplejson
import csv

verify = requests.post("https://osu.ppy.sh/oauth/token", data={"client_id": id, "client_secret": "secret", "grant_type": "client_credentials", "scope": "public", 'Content-type': 'application/json', 'Accept': 'application/json'})
myDict = simplejson.loads(verify._content)
access_token = myDict["access_token"]
headers = {"Authorization": "Bearer " + access_token, 'Content-type':'application/json','Accept':"application/json"}

#with open('out.txt', 'w') as f:
#   with redirect_stdout(f):
#        print(access_token)
#import itertools   
   

for i in range(20):
        req = requests.get("https://osu.ppy.sh/api/v2/rankings/osu/performance", params={"mode": "osu", "type": "performance", "response-type":"code", "cursor[page]":f"{i}"}, headers={"Authorization": f"Bearer {access_token}", 'Content-type':'application/json','Accept':"application/json"})
        request_content = req.content
        actual_content = json.loads(request_content)
       # actual_content = json.dumps(actual_content).replace('\'', "\"").replace("True", "\"True\"").replace("False", "\"False\"").replace("None", "\"None\"")
       # actual_content = simplejson.loads(actual_content)
        rankings = actual_content['ranking']
        
        with open('players.csv', 'a') as file:
                writer = csv.writer(file)
                for player in rankings:
                        writer.writerow([player['user']['username'], player['pp'], player['hit_accuracy'], player['play_count'], player['global_rank']])