#This is a bot discord created by Dralexgon and Mysthieu.
#The purpose of this bot is to roleplay easier with your friends.

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#note, if you want to run this code, you need to create a file called token.txt one directory above the code and put your token in it.
token = open('../token.txt', 'r').readlines()[0]
bot.run(token)