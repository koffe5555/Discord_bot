from asyncio.windows_events import NULL
#from get_anime import FindAnime
import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
import requests
import json

bot = commands.Bot(command_prefix='!')

# Things to run when the bot connects to Discord


@bot.event
async def on_ready():
    print('Connected!')


@bot.command(name="find", pass_context=True)
async def get_anime(ctx):
    
    img = ctx.message.attachments[0]
    url = "https://api.trace.moe/search?url=" + str(img)
    res = requests.get(url)
    res_dict = res.json()

    anilistId = res_dict['result'][0]['anilist']
    match = res_dict['result'][0]['similarity']
    
    title = res_dict['result'][0]['filename']
    splitTitle = title.split(" ")[1:]
    dash = '-'
    fullTitle = ""

    for item in splitTitle:
        if(item == dash):
            break
        fullTitle += item + " "
    
    await ctx.send("Anime: " + fullTitle + "\n" + "Match: " + str(match) + "%" + "\n" + "https://anilist.co/anime/" + str(anilistId))  

@bot.command(name="waifu")
async def get_waifu(ctx, typ: str, category: str):
    url = "https://api.waifu.pics/" + typ + "/" + category
    r = requests.get(url)
    r_dict = r.json()
    img = r_dict['url']
    await ctx.send(img)  

@bot.command(name="waifu-help")
async def waifu_help(ctx):
    help_string = "types: sfw:\n\nwaifu, neko, shinobu, bully, cuddle, kill, megumin, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kick, happy, wink, poke, dance, cringe\n\tNsfw:\n\nwaifu, neko, trap, blowjob"
    await ctx.send(help_string)
    
bot.run('ODYxNjMwMzI3MjczMTYwNzQ0.YOMlxg.k7IJ_o-HN2hOxy9jtpkVSB3FafI')