#This is a bot discord created by Dralexgon and Mysthieu.
#The purpose of this bot is to roleplay easier with your friends.

import discord
from discord.ext import commands

from GameMaster import GameMaster
from Character import Character
from Translate import Translate

bot = commands.Bot(command_prefix='!')

def get_custom_emoji(name):
    return discord.utils.get(bot.emojis, name=name)

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(alias=["createcharacter"])
async def create_character(ctx: commands.Context):
    """
    #the user will respond by typing message in the same channel or by reacting to the message
    await ctx.send(Translate.get("QUESTION_NAME"))
    name = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content

    await ctx.send(Translate.get("QUESTION_GENRE"))
    gender = int((await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content)
    """

    question = await ctx.send(Translate.get("QUESTION_RACE"))
    #for emojiName in ["Human", "DemonBorn", "Sylphe", "Angel", "Sirne"]:
    for emojiName in [  get_custom_emoji("Human"), 
                        get_custom_emoji("DemonBorn"),
                        get_custom_emoji("Sylphe"),
                        get_custom_emoji("Angel"),
                        get_custom_emoji("Sirne")]:
        await question.add_reaction(emojiName)
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    combatClass = reaction.emoji.name
    

    question = await ctx.send(Translate.get("QUESTION_COMBAT_CLASS"))
    for emojiName in ["Garde_sentinelle", "Guerrier_polyvalent", "Tireur_d_elite", "Assassin_furtif", "Mage_de_soutien"]:
        await question.add_reaction(discord.utils.get(bot.emojis, name=emojiName))
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    combatClass = reaction.emoji.name

    question = await ctx.send(Translate.get("QUESTION_MAGIC_CLASS"))
    for emojiName in ["🔥", "💧", "🪨", "💨"]:
        await question.add_reaction(emojiName)
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    magicClass = reaction.emoji.name

    GameMaster.addCharacter(Character(ctx.author.id, name, gender, race, combatClass, magicClass))


#note for me, to wait for an answer, use await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

#note, if you want to run this code, you need to create a file called token.txt one directory before the code and put your token in it.
token = open('../token.txt', 'r').readlines()[0]
bot.run(token)