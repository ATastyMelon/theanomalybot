import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(os.getenv('command_prefix'), intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    print(os.getenv('command_prefix'))
    await client.change_presence(activity=discord.CustomActivity(name="Rotating Ominously"))

@client.command('tyler')
async def ping(ctx):
    await ctx.send("im coming")

@client.command('sex')
async def sex(ctx):
    await ctx.send("I will...")

client.run(os.getenv('bot_token'))