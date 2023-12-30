import discord
import time 
from discord.ext import commands
import random

from bot_mantik import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def options(ctx):
    temp_list = ['$hello', '$pasw', '$bot']
    for element in temp_list:
        await ctx.send(element)
        
bot.run("")