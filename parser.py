import json
import datetime
import sys
from pprint import pprint

with open('stashtab-api.json') as data_file:
  data = json.load(data_file)
  
#pprint(data["stashes"][2])
searchName = "Energy From Within"
searchName2 = "Atziri's Step"
searchName3 = "Tabula Rasa"
searchName4 = "Windripper"
searchName5 = "Added Chaos"
search = searchName
i = 0
j = 0
for i in range(0, len(data["stashes"])-1):
  j = 0
  for j in range(0, len(data["stashes"][i]["items"])-1):
    # Name of the item for livesearch goes here
    if (data["stashes"][i]["items"][j]["name"].startswith("<<set:MS>><<set:M>><<set:S>>" + searchName) or data["stashes"][i]["items"][j]["name"].startswith("<<set:MS>><<set:M>><<set:S>>" + searchName3)) and data["stashes"][i]["items"][j]["league"].startswith("Hardcore Legacy"):
      if not data["stashes"][i]["items"][j]["id"] in open('known_id_list').read():
        print datetime.datetime.now()
        print("itemname: " + (data["stashes"][i]["items"][j]["name"])[28:])
        print("accountName: " + data["stashes"][i]["accountName"])
        print("lastCharacterName: " + data["stashes"][i]["lastCharacterName"])
        print("league: " + data["stashes"][i]["items"][j]["league"])
        print("stash: " + data["stashes"][i]["stash"])
        print("ilvl: " + str(data["stashes"][i]["items"][j]["ilvl"]))
        print("id: " + str(data["stashes"][i]["items"][j]["id"]))
        with open("known_id_list", "a") as myfile:
          myfile.write(str(data["stashes"][i]["items"][j]["id"]) + "\n")
        try:
          print("Note: " + str(data["stashes"][i]["items"][j]["note"]))
        except:
          pass
        try:
          print("sockets: " + str(data["stashes"][i]["items"][j]["sockets"]))
        except:
          pass
        print("corrupted: " + str(data["stashes"][i]["items"][j]["corrupted"]))
        try:
          print("enchantMods: " + str(data["stashes"][i]["items"][j]["enchantMods"]))
        except:
          pass
        try:
          print("implicitMods: " + str(data["stashes"][i]["items"][j]["implicitMods"]))
        except:
          pass
        try:
          print("explicitMods:")
          pprint(data["stashes"][i]["items"][j]["explicitMods"])
        except:
          pass
        try:
          print("additionalProperties: " + str(data["stashes"][i]["items"][j]["additionalProperties"]))
        except:
          pass
        #pprint(data["stashes"][i]["items"][j])
        try:
          print("@" + data["stashes"][i]["lastCharacterName"] + " Hi, I would like to buy your " + (data["stashes"][i]["items"][j]["name"])[28:] + " listed for " + str(data["stashes"][i]["items"][j]["note"]) + " in " + data["stashes"][i]["items"][j]["league"] + " (stashtab: \"" + data["stashes"][i]["stash"] + "\").")
        except:
          print("@" + data["stashes"][i]["lastCharacterName"] + " Hi, I would like to buy your " + (data["stashes"][i]["items"][j]["name"])[28:] + " in " + data["stashes"][i]["items"][j]["league"] + " (stashtab: \"" + data["stashes"][i]["stash"] + "\").")
        print
    j += 1


#bei unid items ueber icon gehen
#pprint(data["stashes"][2]["items"][11]["icon"])
#u'http://web.poecdn.com/image/Art/2DItems/Weapons/TwoHandWeapons/Staves/Staff6unique.png?scale=1&w=2&h=4&v=d2e8ef91b21959805d65c9110d356ada3'
