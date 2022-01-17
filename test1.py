import requests, json, time, os
from api import *

prüfung_mission()


if prüfung_neu == False:
    # Updatet aktuelle Mission
    update()
if prüfung_neu == True:
    # Erstellt neue Mission
    erstellen()
