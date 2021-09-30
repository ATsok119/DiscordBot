#!/usr/bin/python3
from discord.ext import commands
import discord

import os

from main_part import main_cog
from music_part import music_cog
from text_part import text_cog
from rpg_part import rpg_cog

def getToken():
    with open('/home/pi/guppi_token.txt','r') as tfile:
        token = tfile.read()
        
    return token
    
token = getToken()
intents = discord.Intents.all()
intents.members = True
# intents.presence = True

bot = commands.Bot(intents=intents,command_prefix='/')
bot.remove_command('help')

bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))
bot.add_cog(text_cog(bot))
bot.add_cog(rpg_cog(bot))

bot.run(token)