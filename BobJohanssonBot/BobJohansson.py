#!/usr/bin/python3
from discord.ext import commands
import discord
from textFun import *
import d20
import os
import youtube_dl

def convert(s):
    new =''
    for x in s:
        new += x
    return new

def getToken():
    with open('/home/pi/token.txt','r') as tfile:
        token = tfile.read()
        
    return token
    
    
token = getToken()

client = commands.Bot(command_prefix='$')

    
@client.command()
async def roll(ctx, arg : str):
    res  = d20.roll(arg)
    await ctx.send(str(res))
    
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    


@client.command()
async def inspire(ctx):
    quote = getDesQuote()
    await ctx.send(quote['message'])
    
@client.command()
async def hi(ctx):
    await ctx.send('Hello There!\nTest')
    
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Nanana! Im not connected to anything.")
        
        
@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")
    
client.run(token)   