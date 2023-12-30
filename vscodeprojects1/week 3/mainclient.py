import discord
import random
from bot_mantik import gen_pass, rand_emoji, head_tail, greeting_a, send_off_a, feeling_a

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("$good morning"):
        await message.channel.send("morning honey <3")
    elif message.content.startswith("$goodnight"):
        await message.channel.send("nightt, sleep well darlin~")
    elif message.content.startswith("$hello") or message.content.startswith("$hey") or message.content.startswith("$hi"):
        await message.channel.send(greeting_a)
    elif message.content.startswith("$how are you") or message.content.startswith("$whats up") or message.content.startswith("$how are things") or message.content.startswith("$wassup"):
        await message.channel.send(send_off_a())
    elif message.content.startswith("$bye") or message.content.startswith("$farewell") or message.content.startswith("$cya") or message.content.startswith("$see ya") or message.content.startswith("$see you"):
        await message.channel.send(feeling_a())
    elif message.content.startswith("$password"):
        await message.channel.send("created password: " + gen_pass(10))
    elif message.content.startswith("$emoji"):
        await message.channel.send(rand_emoji())
    elif message.content.startswith("$coin"):
        await message.channel.send(head_tail())


client.run("MTE4MzA5Mzk2MDc1NTkyNDk5Mg.GBPVZ5.amhLs8j0amd4O0_-UNNKHt_OcqArYc2q_pkRCc")









