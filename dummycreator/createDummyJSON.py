import random,json


for i in range(20):
    jsonDict = []

    dict1={}
    dict1["label"]="Whatsapp"
    dict1["value"]=str(random.randint(2000,5000))

    dict2 = {}
    dict2["label"] = "Facebook"
    dict2["value"] = str(random.randint(2000, 5000))

    dict3 = {}
    dict3["label"] = "Instagram"
    dict3["value"] = str(random.randint(2000, 5000))

    dict4 = {}
    dict4["label"] = "Zomato"
    dict4["value"] = str(random.randint(2000, 5000))

    dict5 = {}
    dict5["label"] = "Quora"
    dict5["value"] = str(random.randint(2000, 4000))

    dict6 = {}
    dict6["label"] = "Camera"
    dict6["value"] = str(random.randint(2000, 5000))

    dict7 = {}
    dict7["label"] = "Notes"
    dict7["value"] = str(random.randint(2000, 4000))

    dict8 = {}
    dict8["label"] = "Ola"
    dict8["value"] = str(random.randint(2000, 5000))

    dict9 = {}
    dict9["label"] = "Uber"
    dict9["value"] = str(random.randint(2000, 5000))

    jsonDict.append(dict1)
    jsonDict.append(dict2)
    jsonDict.append(dict3)
    jsonDict.append(dict4)
    jsonDict.append(dict5)
    jsonDict.append(dict6)
    jsonDict.append(dict7)
    jsonDict.append(dict8)
    jsonDict.append(dict9)

    with open('user'+str(i)+'.json', 'w') as outfile:
        json.dump(jsonDict, outfile)

# [
#   {
#       "label": "Whatsapp",
#       "value": "4009"
#   },
#   {
#       "label": "Facebook",
#       "value": "3010"
#   },
#   {
#       "label": "Instagram",
#       "value": "749"
#   },
#   {
#       "label": "Zomato",
#       "value": "809"
#   },
#   {
#       "label": "Quora",
#       "value": "1003"
#   },
#   {
#       "label": "Camera",
#       "value": "501"
#   },
#   {
#       "label": "Notes",
#       "value": "889"
#   },
#   {
#       "label": "Ola",
#       "value": "1200"
#   },
#   {
#       "label": "Uber",
#       "value": "978"
#   }
# ]