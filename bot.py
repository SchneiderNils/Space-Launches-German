import requests, json, time, datetime, os, tweepy
from api import *
from dotenv import load_dotenv

# Lädt .env Datei
load_dotenv()

update_abfrage = 0

# Twitter API
api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

prüfung()

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)

update_abfrage = update(update_abfrage)

print(update_abfrage)