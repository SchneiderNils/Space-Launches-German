import requests, json

# Prüft ob es noch die selbe Mission ist.
def prüfung_mission():
    res_launch = requests.get(f"https://api.orbyte.tv/v1/launches")
    launch = res_launch.json()

    with open('next_launch.json','r') as file:
        next = json.load(file)
    uid_p = next['next_launch']['uid']

    if not uid_p == launch['upcoming'][0]['uid']:
        global prüfung_neu
        prüfung_neu = True
    else:
        prüfung_neu = False

# Updatet den Startzeitpunkt
def update():
    res_launch = requests.get(f"https://api.orbyte.tv/v1/launches")
    launch = res_launch.json()
    fileName = "next_launch.json"
    jsonObject = {
        "next_launch": {
            "start": launch['upcoming'][0]['sort_date'],
            "last_update_api": launch['upcoming'][0]['last_update'],
        }, 
    }
    file = open(fileName, "r")
    json.dump(jsonObject, file, indent=4)
    file.close()

# Erstellt JSON mit der nächsten Mission
def erstellen():
    res_launch = requests.get(f"https://api.orbyte.tv/v1/launches")
    launch = res_launch.json()
    fileName = "next_launch.json"
    jsonObject = {
        "next_launch": {
            "uid": launch['upcoming'][0]['uid'],
            "name": launch['upcoming'][0]['name'],
            "mission": launch['upcoming'][0]['mission'],
            "firma": launch['upcoming'][0]['provider'],
            "rocket": launch['upcoming'][0]['vehicle'],
            "pad": launch['upcoming'][0]['pad'],
            "ort": launch['upcoming'][0]['location'],
            "start": launch['upcoming'][0]['sort_date'],
            "erstellt": launch['upcoming'][0]['created'],
            "last_update_api": launch['upcoming'][0]['last_update'],
        }, 
    }
    file = open(fileName, "w")
    json.dump(jsonObject, file, indent=4)
    file.close()
    