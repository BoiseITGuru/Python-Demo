import datetime
import tweepy
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("fcwB0CLT1vcjRIJrosFbyMu9T", "LPGUe4rw7ZFnxAOFMpuPZng7iHslXzTifuRvqlnSXVcQd0zy6V")
auth.set_access_token("1430287632710340608-NT1IOkAKCeMWB2wyRuKJmy8reHndhv", "YQVoWPBVYPv7YtKcwsUQKvuWMbgyo6lsmAI1P9aVsW1Le")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


while True:
    api.update_status("When your enemy’s making mistakes, don’t interrupt him.” – Moneyball (2011)")







