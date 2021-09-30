#!/usr/bin/python3
from discord.ext import commands
import discord
from pathlib import Path

import d20

class rpg_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dm = ''
        self.save = 'saved_data.txt'
        fname = 'saved_data.txt'
        path = Path(fname)
        if not path.is_file():
            with open(fname,'w') as f:
                f.write('')
            
    def getRoll(self, usr, name):
        roll = ''
        with open(self.save, 'r') as file:
            raw = file.read()
            
        for line in raw.split('\n'):
            if usr in line and name in line:
                roll = line.split(';')[2]
        
        return roll
        
    def saveRoll(self, usr, name, roll):
        savestr = usr+';'+name+';'+roll
        
        with open(self.save, 'r') as file:
            raw = file.read()
        
        lines = raw.split('\n')
        for i in range(len(lines)):
            s = usr+';'+name
            if s in lines[i]:
                line[i] = savestr
        if savestr not in lines:
            lines.append(savestr)
        
        outstr = '\n'.join(lines)
        with open(self.save,'w') as file:
            file.write(outstr)
            
    @commands.command(name='r',help='Roll dice with specified values and modifiers')
    async def r(self, ctx, *args):
        r = ''.join(args)
        res = d20.roll(r)
        await ctx.send(str(res))
        
    @commands.command(name='save',help='Save a specific roll')
    async def save(self, ctx, *args):
        arg = ''.join(args)
        usr = ctx.author.name
        s_name = arg.split(';')[0]
        roll = arg.split(';')[1]
        self.saveRoll(usr,s_name,roll)
        await ctx.send('%s Your roll is safe with me...'%(usr))
        
    @commands.command(name='roll',help='roll a specific previous saved roll')
    async def roll(self, ctx, *args):
        rname = ''.join(args)
        usr = ctx.author.name
        r = self.getRoll(usr,rname)
        if r:
            res = d20.roll(r)
            await ctx.send(str(res))
        else:
            await ctx.send("I cant find this specific roll")
        
        