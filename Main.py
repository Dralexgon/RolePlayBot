#This is a bot discord created by Dralexgon and Mysthieu.
#The purpose of this bot is to roleplay easier with your friends.

import discord
from discord.ext import commands

from Character import Character
from Translate import Translate

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
    await ctx.send(Translate.get("QUESTION_NAME"))
    name = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content

    await ctx.send(Translate.get("QUESTION_GENRE"))
    gender = int((await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content)

    question = await ctx.send(Translate.get("QUESTION_RACE"))
    #the bot add a reaction to the message with speficic guild emoji :Humain:, :Sangdedemon:
    #/!\dont work /!\
    await question.add_reaction(discord.utils.get(ctx.guild.emojis, id='1053088370747768884'))
    await question.add_reaction(discord.utils.get(ctx.guild.emojis, id='1053088532618543294'))#"\:1053088532618543294:")
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    race = reaction.emoji.name

    question = await ctx.send(Translate.get("QUESTION_COMBAT_CLASS"))
    await question.add_reaction(":Warrior:")
    await question.add_reaction(":Archer:")
    await question.add_reaction(":Mage:")
    await question.add_reaction(":Assassin:")
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    combatClass = reaction.emoji.name

    question = await ctx.send(Translate.get("QUESTION_MAGIC_CLASS"))
    await question.add_reaction(":Fire:")
    await question.add_reaction(":Water:")
    await question.add_reaction(":Earth:")
    await question.add_reaction(":Air:")
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    magicClass = reaction.emoji.name

    #create the character
    character = Character(name, gender, race, combatClass, magicClass)

#note for me, to wait for an answer, use await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

#note, if you want to run this code, you need to create a file called token.txt one directory above the code and put your token in it.
token = open('../token.txt', 'r').readlines()[0]
bot.run(token)