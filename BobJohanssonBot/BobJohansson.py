#!/usr/bin/python3
import discord
from textFun import getDesQuote

token = 'ODkyMDIyNjYwMzg3NzMzNTI1.YVG21w.tXf_RK7olFnMdzNjHmHCGX3c2Xg'

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