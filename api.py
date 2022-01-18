from turtle import up
import requests, json, time, datetime

res = requests.get('https://api.orbyte.tv/v1/launches')
launch = res.json()

with open('next_launch.json','r') as file:
        obj = json.load(file)

def erstellen():
    orig = datetime.datetime.fromtimestamp(int(launch['upcoming'][0]['sort_date']))
    löschen = orig + datetime.timedelta(minutes=10)
    fileName = "next_launch.json"
    jsonObject = {
        "uid": launch['upcoming'][0]['uid'],
        "name": launch['upcoming'][0]['name'],
        "provider": launch['upcoming'][0]['provider'],
        "rocket": launch['upcoming'][0]['vehicle'],
        "pad": launch['upcoming'][0]['pad'],
        "ort": launch['upcoming'][0]['location'],
        "mission": launch['upcoming'][0]['mission'],
        "uhrzeiten": {
            "start": int(launch['upcoming'][0]['sort_date']),
            "loeschen": löschen.timestamp(),
            "erstellt_api": int(launch['upcoming'][0]['created']),
            "update_api": int(launch['upcoming'][0]['last_update']),
            "update_json": None, 
        },
    }

    file = open(fileName, "w")
    json.dump(jsonObject, file, indent=4)
    file.close()
    start = time.strftime('%A den %d.%m.%Y %H:%M Uhr', time.localtime(int(launch['upcoming'][0]['sort_date']))) 
    print(f"Neuer Mission! {launch['upcoming'][0]['mission']} von {launch['upcoming'][0]['provider']}")
    print(f"Der Start ist für {start} angelegt!")

def update():
    if not obj['uhrzeiten']['update_api'] == launch['upcoming'][0]['last_update']:
        orig = datetime.datetime.fromtimestamp(int(launch['upcoming'][0]['sort_date']))
        löschen = orig + datetime.timedelta(minutes=10)
        fileName = "next_launch.json"
        jsonObject = {
            "uid": launch['upcoming'][0]['uid'],
            "name": launch['upcoming'][0]['name'],
            "provider": launch['upcoming'][0]['provider'],
            "rocket": launch['upcoming'][0]['vehicle'],
            "pad": launch['upcoming'][0]['pad'],
            "ort": launch['upcoming'][0]['location'],
            "mission": launch['upcoming'][0]['mission'],
            "uhrzeiten": {
                "start": int(launch['upcoming'][0]['sort_date']),
                "erstellt_api": int(launch['upcoming'][0]['created']),
                "update_api": int(launch['upcoming'][0]['last_update']),
                "update_json": int(time.time()), 
            },
        }

        file = open(fileName, "w")
        json.dump(jsonObject, file, indent=4)
        file.close()

        start = time.strftime('%A den %d.%m.%Y %H:%M Uhr', time.localtime(int(launch['upcoming'][0]['sort_date'])))
        print(f"Startzeit wurde auf {start} geupdatet!")
    else:
        print("FEHLER!")

def prüfung():
    if obj['uid'] == launch['upcoming'][0]['uid']:
        print("Selbe UID!")
        time.sleep(1.5)
        if obj['uhrzeiten']['start'] == int(launch['upcoming'][0]['sort_date']):
            print("Alles beim selben!")
        else:
            time.sleep(1.5)
            print("Daten werden geupdatet!")
            update()
    else:
        print("Keine Mission gefunden!")
        print("Neue Mission wird rausgesucht!")
        time.sleep(3)
        erstellen()
