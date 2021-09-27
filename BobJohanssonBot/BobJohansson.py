#!/usr/bin/python3
import discord
from textFun import getDesQuote
import sys, os

def getToken():
    with open('/home/pi/token.txt','r') as tfile:
        token = tfile.read()
        
    return token

token = getToken()

client = discord.Client()



@client.event
async def on_ready():
    print('I hame logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hi'):
        await message.channel.send('Hello there!')
    
    if message.content.startswith('!inspire'):
        quote = getDesQuote()
        
        await message.channel.send(quote['message'])
        
client.run(token)  