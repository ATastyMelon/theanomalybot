import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(os.getenv('command_prefix'), intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    print(f"The current prefix is {os.getenv('command_prefix')}")
    await client.change_presence(activity=discord.CustomActivity(name="Rotating Ominously"))

@client.command('ban')
@commands.has_permissions(ban_members = True)
async def bannywanny(ctx, member : discord.Member, reason = None):
    if reason == None:
        await ctx.send("Provide a reason")
    else:
        await ctx.send(f"Alright, {member.name} was banned!")
        await member.ban(reason=reason)

client.run(os.getenv('bot_token'))