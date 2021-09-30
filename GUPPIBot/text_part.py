#!/usr/bin/python3
from discord.ext import commands
import discord

import requests


class text_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def getInsult(self):
        url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
        r = requests.get(url)

        message = r.json()['insult'] 
            
        return message 
        
    def getDesQuote(self):
        url = 'https://demotivational-quotes-api.herokuapp.com/api/quotes/random'
        r = requests.get(url)

        message = r.json()['quote']
            
        return message 
        
    @commands.command(name='insult', help="Insult a specific target")
    async def insult(self, ctx, *args):
        target = "".join(args)
        text = self.getInsult()
        member = discord.utils.get(ctx.channel.members, name=target) 
        text = text + ' <@!%s>'%(member.id)
        await ctx.send(text)
        
    @commands.command(name='inspire', help="Dysplay a inspiring message")
    async def inspire(self, ctx):
        text = self.getDesQuote()
        text = '@everyone ' + text
        allowed_mentions = discord.AllowedMentions(everyone = True)
        await ctx.send(content = text, allowed_mentions = allowed_mentions)