import discord
from discord.ext import commands
from discord.ext import tasks
import random
import asyncio
from bot_mantik import gen_pass, rand_emoji, head_tail

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma

bot = commands.Bot(command_prefix='$', intents=intents)

######################################################################################?

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

########################################################################
            
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 0  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 0,  # ID of the role associated with unicode emoji '🔴'.
            discord.PartialEmoji(name='🟡'): 0,  # ID of the role associated with unicode emoji '🟡'.
            discord.PartialEmoji(name='green', id=0): 0,  # ID of the role associated with a partial emoji's ID.
        }

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally, add the role.
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        try:
            # Finally, remove the role.
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
########################################################################
        
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')

########################################################################

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(1234567)  # channel ID goes here
        self.counter += 1
        await channel.send(self.counter)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in

######################################################################################?

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı")

@bot.command(name='secret_command')
async def _bot(ctx):
    """love"""
    await ctx.send("shh this bot loves you") 
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"hi! {bot.user}!")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)   

@bot.command()
async def goodnight(ctx):
    await ctx.send(f"sleep well {bot.user} <3")

@bot.command()
async def goodmorning(ctx):
    await ctx.send(f"morning {bot.user} :3")

@bot.command()
async def password(ctx):
    await ctx.send(f"created password: {gen_pass(10)}")

@bot.command()
async def emoji(ctx):
    await ctx.send(rand_emoji())

@bot.command()
async def coin(ctx):
    await ctx.send(head_tail())

@bot.command()
async def bye(ctx):
    await ctx.send(f"see ya! {bot.user}!")

@bot.command()
async def help(ctx):
    """explaining the commands"""
    await ctx.send("$bye: sending off \n $hello: greeting \n $heh: laugh \n $coin: head or tail \n $emoji: random emoji \n $goodnight: wishing a good night \n $password: random password \n $goodmorning: wishing a good morning \n secret_command: ?")


bot.run("MTE4MzA5Mzk2MDc1NTkyNDk5Mg.GBPVZ5.amhLs8j0amd4O0_-UNNKHt_OcqArYc2q_pkRCc")


