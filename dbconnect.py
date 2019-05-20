#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyrebase

config = {
    "apiKey": "AIzaSyDNyT41R1AXYpp6k7xP3m4S_EIUGibcj8s",
    "authDomain": "trape-py-1554172486593.firebaseapp.com",
    "databaseURL": "https://trape-py-1554172486593.firebaseio.com",
    "projectId": "trape-py-1554172486593",
    "storageBucket": "trape-py-1554172486593.appspot.com",
    "messagingSenderId": "415942529071"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


