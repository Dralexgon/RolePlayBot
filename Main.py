#This is the part of the program that interact with discord.

import discord
from discord.ext import commands

from GameManager import GameManager
from Character import Character
from Translate import Translate


bot = commands.Bot(command_prefix='!')

def get_custom_emoji(name):
    return discord.utils.get(bot.emojis, name=name)

@bot.event
async def on_ready():
    print('Bot is ready')


#Always possibles commands :



@bot.command(name="ping", help="This is use to check if the bot is online and working.")
async def ping(ctx):
    await ctx.send("pong")



@client.command(name="help", help="Shows this message.")
async def help(ctx):
    embed = discord.Embed(
        title = "Help",
        colour = discord.Colour.blue()
    )
    commandListinversed = []
    for command in client.commands:
        commandListinversed.append(command)
    for command in commandListinversed:
        embed.add_field(name=command.name, value=command.help, inline=False)
    await ctx.send(ctx.author.mention, embed=embed)



@bot.command(alias=["createcharacter","newcharacter","newchar","createchar"])
async def create_character(ctx: commands.Context):
    #the user will respond by typing message in the same channel or by reacting to the message


    await ctx.send(Translate.get("QUESTION_NAME"))
    #check if the name is already taken
    exist = True
    while exist:
        name = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content
        exist = False
        for character in GameManager.characters:
            if character.name == name:
                exist = True
                await ctx.send(Translate.get("ALREADY_EXIST"))
                break


    await ctx.send(Translate.get("QUESTION_GENRE"))
    gender = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content


    question = await ctx.send(Translate.get("QUESTION_RACE"))
    for emojiName in [  get_custom_emoji("Human"), 
                        get_custom_emoji("DemonBorn"),
                        get_custom_emoji("Sylphe"),
                        get_custom_emoji("Angel"),
                        get_custom_emoji("Sirne")]:
        await question.add_reaction(emojiName)
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    race = reaction.emoji.name


    question = await ctx.send(Translate.get("QUESTION_COMBAT_CLASS"))
    for emojiName in ["Garde_sentinelle", "Guerrier_polyvalent", "Tireur_d_elite", "Assassin_furtif", "Mage_de_soutien"]:
        await question.add_reaction(discord.utils.get(bot.emojis, name=emojiName))
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    combatClass = reaction.emoji.name


    question = await ctx.send(Translate.get("QUESTION_MAGIC_CLASS"))
    for emojiName in ["🔥", "💧", "🪨", "💨"]:
        await question.add_reaction(emojiName)
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    magicClass = reaction.emoji


    GameManager.add_character(Character(ctx.author.id, name, gender, race, combatClass, magicClass))

    await ctx.send(Translate.get("CHARACTER_CREATED"))
    await ctx.send(GameManager.get_character_by_owner_id(ctx.author.id).get_profile_card())




@bot.command(alias=["profile", "profilecard", "characterprofile", "showcharacter", "showcharacterprofile"])
async def show_profile_card(ctx: commands.Context):
    character = GameManager.get_character_by_owner_id(ctx.author.id)
    if character == None:
        await ctx.send("You do not have a character yet.")
    else:
        await ctx.send(character.get_profile_card())


#note, if you want to run this code, you need to create a file called token.txt one directory before the code and put your token in it.
token = open('../token.txt', 'r').readlines()[0]
bot.run(token)


#note for me, 
#to wait for an answer, use await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
#to get a user from an id, use bot.get_user(user_id) 