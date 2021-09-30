#!/usr/bin/python3
from discord.ext import commands
import discord
import asyncio


class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
General commands:
/help - displays all the available commands
Text commands:
/insult <target> - insult the specific target
/inspire - display a inpiring message
Music commands:
/play <keywords> - finds the song on youtube and plays it in your current channel
/queue - displays the current music queue
/skip - skips the current song being played
/pause - pause the current music
/leave - leave the current channel
RPG commands:
/r <keywords> - rolls dice acording to specifications
/save <name>;<keywords> - save a specific rolls
/roll <name> - roll a specific roll
```
"""
        self.text_channel_list = []
           
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
            
            
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        
        if not member.id == self.bot.user.id:
            return

        elif before.channel is None:
            voice = after.channel.guild.voice_client
            time = 0
            while True:
                await asyncio.sleep(1)
                time = time + 1
                if voice.is_playing() and not voice.is_paused():
                    time = 0
                if time == 60:
                    await voice.disconnect()
                if not voice.is_connected():
                    break
