import discord
import time 
from discord.ext import commands
import random
import requests
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} giriş yaptı')


@bot.command()
async def pollution(ctx):
    info_message = "Environmental pollution refers to the introduction of contaminants into the natural environment, causing adverse changes. This can include air pollution, water pollution, soil pollution, and more. Stay informed and take steps to reduce your environmental impact."
    await ctx.send(info_message)


@bot.command()
async def littering(ctx):
    info_message = "Littering has severe consequences on the environment, wildlife, and human health. It can lead to pollution of water bodies, harm to animals that ingest or get entangled in litter, and the spread of diseases. Let's work together to keep our environment clean and safe for everyone."
    await ctx.send(info_message)


@bot.command()
async def responsible(ctx):
    tips = [
        "Always use designated trash bins for your waste.",
        "Separate recyclables from non-recyclables to promote recycling.",
        "Dispose of hazardous materials, such as batteries and electronics, at designated collection points.",
        "Participate in community clean-up events to contribute to a cleaner environment.",
        "Educate others about the importance of responsible waste disposal."
    ]
    
    tip_message = "\n".join(tips)
    await ctx.send(f"Here are some tips for responsible waste disposal:\n{tip_message}")


@bot.command()
async def tips(ctx):
    tips = [
        "Use reusable bags to reduce plastic waste.",
        "Conserve water by fixing leaks and using water-saving appliances.",
        "Opt for eco-friendly transportation options like walking, biking, or using public transit.",
        "Reduce energy consumption by using energy-efficient appliances and turning off lights when not needed.",
        "Properly dispose of waste and recycle materials whenever possible."
    ]
    
    tip_message = "\n".join(tips)
    await ctx.send(f"Here are some tips to help reduce environmental pollution:\n{tip_message}")


#https://openweathermap.org/appid
@bot.command()
async def aqi(ctx):
    api_key = 'your_api_key'
    location = 'turkey'
    
    api_url = f'https://api.example.com/aqi?location={location}&api_key={api_key}'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        aqi_value = data.get('aqi')
        await ctx.send(f"The current Air Quality Index (AQI) for {location} is {aqi_value}.")
    else:
        await ctx.send("Failed to fetch AQI data. Please try again later.")


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('mem'))
    with open(f'mem/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)




        
bot.run("")