# bot.py
import os
import random
import re
from urllib import response
from xml.etree.ElementTree import tostring
import discord

from discord.ext import commands
from dotenv import load_dotenv

from datetime import date

#Variables
warMembers = ["test 1", "test 2", "test 3", "test 4"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')




@bot.command(name='cocName' , help="changes your nickname (!cocName + newName)")
async def changeNickName(ctx, cocName):
    newNickName = cocName
    author = ctx.message.author
    await author.edit(nick = newNickName)
    await ctx.send(f"Nick name was changed for {author.name}")
    
    
@bot.command(name='backOut', help="takes you out of war")
async def backOut(ctx):
    author = ctx.message.author
    userName = author.nick
    allowed = 0
    
    for member in warMembers:
        if member == userName:
            allowed += 1
        
    if allowed == 1:
        warMembers.remove(userName)
        response = "You have been taken out of this war!"
        await ctx.send(response)
    else:        
        response = "You are not registered in this war so you don't need to back out"
        await ctx.send(response)


@bot.command(name='register', help="Register for upcomming war")
async def register(ctx):
    author = ctx.message.author
    userName = author.nick
    allowed = 0
    
    for member in warMembers:
        if member == userName:
            allowed += 1
        
    if allowed == 1:
        response = "You have already registered for this war!"
        await ctx.send(response)
    else:        
        if len(warMembers) < 15:
            warMembers.append(userName)
            response = userName + " has been entered into the war"
            await ctx.send(response)
        else:
            response = "Sorry, but all the war positions have been taken!"
            await ctx.send(response)
        

@bot.command(name='warQueue', help="Shows whos registered for upcomming war")
async def showWarQueue(ctx):
    membersCount = len(warMembers)
    allSpots = 15
    availableSpots = allSpots - membersCount
    
    str = "";

    
    for member in warMembers:
        if member == warMembers[-1]:
            str +=  member + ". "
        else:
            str +=  member + ", "
    
    response = "There are currently {} spots open. Here's the list of participating members: {}".format(availableSpots, str)
    await ctx.send(response)
        
    
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to my Battling saxons discord! To view the list of all the currently available commands type !help'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'test':
        response = "Testing done, working at 100%"
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    
    await bot.process_commands(message)
    

bot.run(TOKEN)