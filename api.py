<<<<<<< HEAD
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
    
=======
from turtle import up
import requests, json, time, datetime, os, tweepy
from dotenv import load_dotenv

# Lädt .env Datei
load_dotenv()

# Twitter API
api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

res = requests.get('https://api.orbyte.tv/v1/launches')
launch = res.json()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    LINE = '============================================================================='


with open('next_launch.json','r') as file:
        obj = json.load(file)

def url():
    print(f"{bcolors.OKCYAN}URL wird erstellt!{bcolors.ENDC}")
    short = "https://api.short.io/links"
    payload = {
        "allowDuplicates": False,
        "originalURL": f"https://www.orbyte.tv/launch/{launch['upcoming'][0]['slug']}",
        "domain": "orburl.de",
        "title": f"{launch['upcoming'][0]['slug']}"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "sk_b2heK3m4SZt3x1Y7"
    }

    url_res = requests.request("POST", short, json=payload, headers=headers)
    
    global shortURL
    shortURL = url_res.json()
    print(f"{bcolors.OKCYAN}URL wurde erstellt{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}--->{shortURL['secureShortURL']}<---{bcolors.ENDC}")
    print(bcolors.LINE)
def erstellen():
    time.sleep(3)
    url()
    print(f"{bcolors.OKCYAN}Daten werden geladen.{bcolors.ENDC}")
    time.sleep(1)
    print(f"{bcolors.OKGREEN}Darten wurden geladen!{bcolors.ENDC}")
    fileName = "next_launch.json"
    jsonObject = {
        "uid": launch['upcoming'][0]['uid'],
        "name": launch['upcoming'][0]['name'],
        "slug": launch['upcoming'][0]['slug'],
        "provider": launch['upcoming'][0]['provider'],
        "rocket": launch['upcoming'][0]['vehicle'],
        "pad": launch['upcoming'][0]['pad'],
        "ort": launch['upcoming'][0]['location'],
        "mission": launch['upcoming'][0]['mission'],
        "website": shortURL['secureShortURL'],
        "twitter_id": None,
        "uhrzeiten": {
            "start": int(launch['upcoming'][0]['sort_date']),
            "erstellt_api": int(launch['upcoming'][0]['created']),
            "update_api": int(launch['upcoming'][0]['last_update']),
            "update_json": None, 
        },
    }

    file = open(fileName, "w")
    json.dump(jsonObject, file, indent=4)
    file.close()
    start = time.strftime('%A den %d.%m.%Y %H:%M Uhr', time.localtime(int(launch['upcoming'][0]['sort_date']))) 
    print(bcolors.LINE)
    print(f"{bcolors.OKBLUE}Mission: {launch['upcoming'][0]['mission']}")
    print(f"{bcolors.OKBLUE}Firma: {launch['upcoming'][0]['provider']}")
    print(f"{bcolors.OKBLUE}Rakete: {launch['upcoming'][0]['vehicle']}")
    print(f"Start: {start}{bcolors.ENDC}")
    print(bcolors.LINE)

    global prüfung_aktuell
    prüfung_aktuell = 1
def update():
    if not obj['uhrzeiten']['update_api'] == launch['upcoming'][0]['last_update']:
        orig = datetime.datetime.fromtimestamp(int(launch['upcoming'][0]['sort_date']))
        löschen = orig + datetime.timedelta(minutes=10)
        fileName = "next_launch.json"
        jsonObject = {
            "uid": launch['upcoming'][0]['uid'],
            "name": launch['upcoming'][0]['name'],
            "slug": launch['upcoming'][0]['slug'],
            "provider": launch['upcoming'][0]['provider'],
            "rocket": launch['upcoming'][0]['vehicle'],
            "pad": launch['upcoming'][0]['pad'],
            "ort": launch['upcoming'][0]['location'],
            "mission": launch['upcoming'][0]['mission'],
            "twitter_id": obj['twitter_id'],
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
        global prüfung_aktuell
        prüfung_aktuell = 2
    else:
        print("FEHLER!")
def prüfung():
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{bcolors.LINE}")
    print(f"{bcolors.OKCYAN}Missionsdaten werden geprüft!{bcolors.ENDC}")
    print(bcolors.LINE)
    time.sleep(1.5)
    if obj['uid'] == launch['upcoming'][0]['uid']:
        print(f"{bcolors.OKCYAN}UID wird geprüft!{bcolors.ENDC}")
        print(bcolors.LINE)
        time.sleep(1.5)
        if obj['uhrzeiten']['start'] == int(launch['upcoming'][0]['sort_date']):
            print(f"{bcolors.OKGREEN}Alle Missionsdaten sind aktuell!{bcolors.ENDC}")
            print(bcolors.LINE)
            global prüfung_aktuell
            prüfung_aktuell = 3
        else:
            time.sleep(1.5)
            print(f"{bcolors.WARNING}Warning: Daten nicht mehr aktuell!{bcolors.ENDC}")
            print(f"{bcolors.OKCYAN}Neue Missionsdaten werden geladen!{bcolors.ENDC}")
            print(bcolors.LINE)
            update()
    else:
        print(f"{bcolors.WARNING}Warning: Keine Mission gefunden!{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Neue Mission wird rausgesucht!{bcolors.ENDC}")
        print(bcolors.LINE)
        erstellen()
def senden():
    if prüfung_aktuell == 1:
        authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
        authenticator.set_access_token(access_token, access_token_secret)
        api = tweepy.API(authenticator, wait_on_rate_limit=True)
        start = time.strftime('%d.%m.%Y, %H:%M Uhr', time.localtime(int(launch['upcoming'][0]['sort_date'])))

        neuer_tweet = f"Es steht eine neue Mission an!\nStart: {start}\n\nMissionsname: {obj['mission']}\nFirma: {obj['provider']}\nRakete: {obj['rocket']}\n\nStartplatz: {obj['ort']}\nLaunchpad: {obj['pad']}\n\n Mehr Infos auf: {obj['website']}\n"

        api.update_status(neuer_tweet)
        print(f"{bcolors.OKGREEN}Tweet ist raus!{bcolors.ENDC}")
        print(bcolors.LINE)
        print(f"{bcolors.OKCYAN}Status ID wird rausgesucht.{bcolors.ENDC}")
        print(bcolors.LINE)
        time.sleep(10)
        timeline = api.user_timeline(user_id=1481748872615677952)
        for info in timeline[:1]:
            id = info.id
        a_file = open("next_launch.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        json_object["twitter_id"] = id
        a_file = open("next_launch.json", "w")
        json.dump(json_object, a_file, indent=4)
        print(f"{bcolors.OKGREEN}ID wurde gefunden!{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Status ID: {id}{bcolors.ENDC}")
        print(bcolors.LINE)
        a_file.close()
    elif prüfung_aktuell == 2:
        alter_tweet = f"https://twitter.com/launch_german/status/{obj['twitter_id']}"
        authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
        authenticator.set_access_token(access_token, access_token_secret)
        api = tweepy.API(authenticator, wait_on_rate_limit=True)
        start = time.strftime('%d.%m.%Y, %H:%M Uhr', time.localtime(int(launch['upcoming'][0]['sort_date'])))

        update_tweet = f"Die {obj['mission']} Mission wurde verschoben!\nSie startet jetzt am {start}"

        api.update_status(update_tweet, attachment_url=alter_tweet)
    elif prüfung_aktuell == 3:
        print(f"{bcolors.OKCYAN}Keine neuen Missionsdaten vorhanden!{bcolors.ENDC}")
        print(bcolors.LINE)
    else:
        print(f"{bcolors.BOLD}{bcolors.FAIL}ERROR: Keine aktuellen Missionsdaten vorhanden!{bcolors.ENDC}")
>>>>>>> c7d33816a629aa84b9709c0771f47a01a7966586
