############
#imports
############
############
#Python 3.6
############
import discord
import random
from random import randint
from discord.ext.commands import bot
from discord.ext import commands
global num
import asyncio
from urllib import request
import re
import os
import datetime
global prismatology

prismatology = {}


from discord import Channel

#void imports
  
num = None
#to do:
#   maybe:
#       image fetcher
#       swear checker
#       weather
#       join leave


#command prefix

Client = discord.Client
bot_prefix = "|"
client = commands.Bot(command_prefix=bot_prefix)
serv = discord.client.Server
channel = discord.utils.get(client.get_all_channels(), name = "general")
#tells you that the bot is running


@client.event
async def on_ready():
  print("Initialized.")
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')
  await client.change_presence(game=discord.Game(name='say |commandhelp'))





#rolls a dice, figure out how to use error handler to handle missing num argument

@client.command(pass_context=True)
async def roll(ctx, num):
  a = int(num) - int(num) + 1
  await client.say("Roll from 1 to {}:".format(num))
  await client.say(randint(a, int(num)))

#tries to replaces your bs with b emojis
@client.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
  if member is None:
    member = ctx.message.author

  await client.say('{0} joined at {0.joined_at}'.format(member))



@client.command(pass_context=True)
async def calculator(ctx, a, b, c):
  o = "{} {} {} is {}"
  if b == '+':
    d = int(a) + int(c)
    o = o.format(a, b, c, d)
    await client.say(o)

  elif b == '-':
    d = int(a) - int(c)
    o = o.format(a, b, c, d)
    await client.say(o)

  elif b == 'x' or b == '*':
    d = int(a) * int(c)
    o = o.format(a, b, c, d)
    await client.say(o)

  elif b == '/':
    d = float(a) / float(c)
    o = o.format(a, b, c, d)
    await client.say(o)
  
  
@client.command(pass_context=True)
async def commandhelp(ctx):
  helpmessage = """
Hi, I'm Richardbot, and I can do things.
Command prefix, |, type | before commands
|roll x, rolls a dice, type |roll and then the dice number.
|calculator a b c, does math, a is the first number, b is the operation, c is the second number.
|flip, flips a coin!
|eightball, gives you a virtual 8ball fortune.
|say, richardbot repeats what you said!
|ytsearch, searches on youtube for what you asked and gives the first result.
|invite, gives you a bot invite.  
|censor, censors what you said.
|joined_at, prints when you joined.
This bot was created by Flammable.


Twitter: @Flammabl3_
Reddit: /u/Flammable_
steam: https://steamcommunity.com/id/somethingsburning/
Discord: #7154
"""

  await client.say(helpmessage)
  
@client.command(pass_context=True)
async def flip(ctx):
  #commented out code is code that I have to figure out later
  a = ctx.message.channel
  coinflip = randint(0, 2)
  if coinflip == 0:
    await client.say('Heads!')
    await client.send_file(a, 'asset/heads.png')
  elif coinflip == 1:
    await client.say('Tails!')
    await client.send_file(a, 'asset/tails.png')

@client.command(pass_context=True)
async def eightball(ctx):
  answers = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again'
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
  ]
  await client.say(random.choice(answers))
@client.command(pass_context=True)
async def say(ctx, *phrase):
  full_phrase = []
  for i in phrase:
    full_phrase.append(i)
  final = ' '.join(full_phrase)
  await client.say(final)

@client.command(pass_context=True)
async def ytsearch(ctx, *query):
  query_list = []
  for i in query:
    query_list.append(i)
    
  
  if len(query_list) == 1:
    url = "https://www.youtube.com/results?search_query={}".format(query)
    hdr = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36',
    }
    urlrequest = request.Request(url, headers=hdr)
    page = request.urlopen(urlrequest)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', page.read().decode())
  else:
    multiple_query = '+'.join(query_list)
    url = "https://www.youtube.com/results?search_query={}".format(multiple_query)
    hdr = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36',
    }
    urlrequest = request.Request(url, headers=hdr)
    page = request.urlopen(urlrequest)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', page.read().decode())
    
      

  await client.say('https://www.youtube.com/watch?v=' + search_results[1])

'''
@client.command(pass_context=True)
async def indicator(ctx, *args):
  b = []
  for i in args:
    if i == 'a':
      i = ':regional_indicator_u:'
      b.append(i)
    if i == 'e':
      i = ':regional_indicator_e:'
      b.append(i)
    if i == 'i':
      i = ':regional_indicator_i:'
      b.append(i)
    if i == 'o':
      i = ':regional_indicator_o:'
      b.append(i)     
    if i == 'u':
      i = ':regional_indicator_u:'
      b.append(i)
    else:
      b.append(i)
    await client.say(''.join(b))
'''
@client.command(pass_context=True)
async def censor(ctx, *args):
  b = []
  for i in args:
    i = '█' * len(i)
    b.append(i)
  await client.say(''.join(b))

#add a dang prismatology thing


@client.command(pass_context=True)
async def invite(ctx):
  await client.say("")
#figure out how to use to incorporate id for stuff

client.run("")
