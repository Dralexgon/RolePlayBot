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

@bot.command()
async def create_character(ctx):
    #the user will respond by typing message in the same channel or by reacting to the message
    await ctx.send("What is your character's name ?")
    name = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    await ctx.send("What is your character's age ?")
    age = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    question = await ctx.send("What is your character race ?")
    #add emojis to choose
    await question.add_reaction(':Human:')
    await question.add_reaction(':Sangdedemon:')

#note for me, to wait for an answer, use await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

#note, if you want to run this code, you need to create a file called token.txt one directory above the code and put your token in it.
token = open('../token.txt', 'r').readlines()[0]
bot.run(token)