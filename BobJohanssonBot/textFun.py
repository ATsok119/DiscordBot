#!/usr/bin/python3
import requests
import random

def rollDice(number,sides):
    rolls = []
    for d in range(number):
        roll = random.randint(1,sides)
        rolls.append(roll)
        
    return rolls

def getDesQuote():
    url = 'https://demotivational-quotes-api.herokuapp.com/api/quotes/random'
    r = requests.get(url)

    message = {}
    message['message'] = r.json()['quote']
    message['author'] = r.json()['author']
        
    return message 
    
def getInsult():
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    r = requests.get(url)

    message = r.json()['insult'] 
        
    return message 