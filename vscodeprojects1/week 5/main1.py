import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def lol(ctx):
    img_name = random.choice(os.listdir('images2'))
    with open(f'images2/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

#@bot.command()
#async def mem(ctx):
#    with open('vscodeprojects/images/meme1.png', 'rb') as f:
#        picture = discord.File(f)
#    await ctx.send(file=picture)


bot.run("MTE4MzA5Mzk2MDc1NTkyNDk5Mg.GfXVR2.nF2eLvYYHx8pTI3_h2HTeJt3adDwA34FK2HTmQ")