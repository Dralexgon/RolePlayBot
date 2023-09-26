#This is the part of the program that interact with discord.

import discord
from discord.ext import commands

from GameManager import GameManager
from Character import Character
from Translate import Translate
from Item import Item
from Region import Region


bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())
GameManager = GameManager()

def get_custom_emoji(name):
    return discord.utils.get(bot.emojis, name=name)

@bot.event
async def on_ready():
    print('Bot is ready')


#Always possibles commands :



@bot.command(name="ping", help="This is use to check if the bot is online and working.")
async def ping(ctx):
    await ctx.send("pong")



@bot.command(
    name="help",
    help="Shows this message.")
async def help(ctx):
    embed = discord.Embed(
        title = "Help",
        colour = discord.Colour.blue()
    )
    commandListinversed = []
    for command in bot.commands:
        commandListinversed.append(command)
    for command in commandListinversed:
        embed.add_field(name=command.name, value=command.help, inline=False)
    await ctx.send(ctx.author.mention, embed=embed)



@bot.command(
    name="create_character",
    help="Start a conversation to create your character step by step",
    aliases=["createcharacter","newcharacter","newchar","createchar"])
async def create_character(ctx: commands.Context):
    #the user will respond by typing message in the same channel or by reacting to the message


    await ctx.send(Translate.get("character_creation.question.name"))
    #check if the name is already taken
    exist = True
    while exist:
        name = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content
        exist = False
        for character in GameManager.characters:
            if character.surname == name:
                exist = True
                await ctx.send(Translate.get("character_creation.already_exist"))
                break


    await ctx.send(Translate.get("character_creation.question.genre"))
    gender = (await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)).content


    question = await ctx.send(Translate.get("character_creation.question.race"))
    for emojiName in [  get_custom_emoji("Human"), 
                        get_custom_emoji("DemonBorn"),
                        get_custom_emoji("Sylphe"),
                        get_custom_emoji("Angel"),
                        get_custom_emoji("Sirne")]:
        await question.add_reaction(emojiName)
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    race = reaction.emoji.name


    question = await ctx.send(Translate.get("character_creation.question.combat_class"))
    for emojiName in ["Garde_sentinelle", "Guerrier_polyvalent", "Tireur_d_elite", "Assassin_furtif", "Mage_de_soutien"]:
        await question.add_reaction(discord.utils.get(bot.emojis, name=emojiName))
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    combatClass = reaction.emoji.name


    question = await ctx.send(Translate.get("character_creation.question.magic_class"))
    for emojiName in ["🔥", "💧", "🪨", "💨"]:
        await question.add_reaction(emojiName)
    reaction, user = await bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.message == question)
    magicClass = reaction.emoji


    GameManager.add_character(Character(ctx.author.id, name, gender, race, combatClass, magicClass))

    await ctx.send(Translate.get("character_creation.created"))
    await ctx.send(GameManager.get_character_by_owner_id(ctx.author.id).get_profile_card())




@bot.command(
    name="show_profile_card",
    help="Shows the profile card of your character",
    aliases=["profile", "card", "character", "show_profile", "show_card"])
async def show_profile_card(ctx: commands.Context):
    character = GameManager.get_character_by_owner_id(ctx.author.id)
    if character == None:
        await ctx.send("You don't have a character yet.")
        return
    
    await ctx.send(character.get_profile_card())



@bot.command(
    name="exploration",
    help="Your character explore arround and gain loots specific of your current region.",
    aliases=["explo"])
async def exploration(ctx: commands.Context):
    character = GameManager.get_character_by_owner_id(ctx.author.id)

    if character == None:
        await ctx.send(Translate.get("error.no_character"))
        return
    if len(character.region.loots) == 0:
        await ctx.send(Translate.get("error.no_loot_region"))
        return
    
    item: Item = character.region.get_random_reward()
    character.inventory.append(item)
    character.save_as_pickle()
    await ctx.send(Translate.get("item.receive") + "1x " + Translate.get(item.name) + " !")


@bot.command(
    name="move",
    help="Your character move to another region.",
    alias=["move"])
async def move(ctx: commands.Context, *args):
    user: discord.Member = ctx.author
    character = GameManager.get_character_by_owner_id(user.id)
    if character == None:
        await ctx.send("You don't have a character yet.")
        return

    await user.remove_roles(discord.utils.get(user.guild.roles, name=character.region.name))
    character.region = Region.get_by_name(args[1])
    await user.add_roles(discord.utils.get(user.guild.roles, name=Translate.get(character.region.name)))

#note, if you want to run this code, you need to create a file called token.txt one directory before the code and put your token in it.
token = open('../token.txt', 'r').readlines()[0]
bot.run(token)


#note for me, 
#to wait for an answer, use await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
#to get a user from an id, use bot.get_user(user_id) 