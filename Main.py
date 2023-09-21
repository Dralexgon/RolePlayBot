#This is a bot discord created by Dralexgon and Mysthieu.
#The purpose of this bot is to manage a roleplay server.

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


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(alias=["createcharacter","newcharacter","newchar","createchar"])
async def create_character(ctx: commands.Context):
    #the user will respond by typing message in the same channel or by reacting to the message


    await ctx.send(Translate.get("QUESTION_NAME"))
    name = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content
    #check if the name is already taken
    exist = False
    for character in GameManager.characters:
        if character.surname == name:
            exist = True
            break
    while exist:
        await ctx.send(Translate.get("ALREADY_EXIST"))
        name = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content
        exist = False
        for character in GameManager.characters:
            if character.name == name:
                exist = True
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

#Gamemaster commands :


@bot.command(aliases=["startgame", "start"])
async def start_game(ctx: commands.Context):
    for game in GameManager.games:
        if game.gameMasterID == ctx.author.id:
            await ctx.send(Translate.get("ALREADY_IN_GAME"))
            return
    
    GameManager.new_game(ctx.author.id)

    await ctx.send(Translate.get("GAME_CREATED"))


@bot.command(aliases=["newmap", "createmap", "addmap", "map"])
async def change_map(ctx: commands.Context, mapName: str):
    map = GameManager.get_map(mapName)
    message: discord.Message = await ctx.send(map.get_image())

    #for player in characterNames:

    #message.edit(content=map.get_image())


#note, if you want to run this code, you need to create a file called token.txt one directory before the code and put your token in it.
token = open('../token.txt', 'r').readlines()[0]
bot.run(token)


#note for me, 
#to wait for an answer, use await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
#to get a user from an id, use bot.get_user(user_id) 