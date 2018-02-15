#yes my code sucks 
#yes I forgot why added around a third of all the variables
#chill
#I only added comments now because I'm lazy and no one will see this code

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


#ignore this I think  
num = None
#to do:
#   maybe:
#       image fetcher (imgur api? it's a hassle though)
#       weather
#       join leave messages


#command prefix for commands
#the client
Client = discord.Client
bot_prefix = "|"
client = commands.Bot(command_prefix=bot_prefix)
#the server (duh)
serv = discord.client.Server
channel = discord.utils.get(client.get_all_channels(), name = "general")
#tells you that the bot is running

#boots it up and tells you a bunch of stuff
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
  a = int(num) - int(num) + 1 #a = none - none + 1, so a = 1? 
                              #what was I doing here don't touch it it might break
  await client.say("Roll from 1 to {}:".format(num))
  await client.say(randint(a, int(num)))

#tells you when you joined but I have no clue what the None bit is about disregard
@client.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
  if member is None:
    member = ctx.message.author

  await client.say('{0} joined at {0.joined_at}'.format(member))


#does quick maths
@client.command(pass_context=True)
async def calculator(ctx, a, b, c): #a is the first number, b is the operator, c is the second
  o = "{} {} {} is {}"              #number, d is the answer
  if b == '+':
    d = int(a) + int(c)
    o = o.format(a, b, c, d)
    await client.say(o)
#add subtract multiply divide
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
|attack, attacks a user.
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
#eightball, self explanatory
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
#says what you said to it, functions that take *args assemble the phrase with join()
@client.command(pass_context=True)
async def say(ctx, *phrase):
  full_phrase = []
  for i in phrase:
    full_phrase.append(i)
  final = ' '.join(full_phrase)
  await client.say(final)
#looks stuff up on youtube and gives you the first result
@client.command(pass_context=True)
async def ytsearch(ctx, *query):
  query_list = []
  for i in query:
    query_list.append(i) #same deal as with the say command
    
  #added this so it doesn't add a '+' symbol to 1 unseperated query, useless because
  #a + at the end is automatically truncated and it doesn't affect it anyways
  if len(query_list) == 1:
    url = "https://www.youtube.com/results?search_query={}".format(query) #uses requests
    #headers so youtube doesn't deny access because it's a bot
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
#regional indicator command, didn't work though
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
#spits out what you said but with the '█' character replacing everything
@client.command(pass_context=True)
async def censor(ctx, *args):
  b = []
  for i in args:
    i = '█' * len(i)
    b.append(i)
  await client.say(''.join(b))
#a command for having randomised and absurd physical combat
@client.command(pass_context=True)
async def attack(ctx, *attacked):
  attacked_user = ' '.join(attacked)
  #organs that can be attacked and the ways you can attack them
  organs = ['big toe', 'toenail', 'pinky toe', 'toe', 'ankle', 'calf', 'knee', 'kneecap', 'thigh',
            'radial artery', 'thigh', 'femur', 'tibia', 'penis', 'testicles', 'scrotum', 'vagina', 'ovaries',
            'intestines', 'spleen', 'stomach', 'liver', 'kidneys', 'ribs', 'ribcage', 'heart', 'lungs', 'spine', 'tailbone',
            'spinal cord', 'back', 'chest', 'shoulder blade', 'arm', 'wrist', 'pinky', 'thumb', 'finger',
            'shoulder', 'throat', 'trachea', 'esophagus', 'eyeballs', 'nose', 'septum', 'frenulum', 'vulva', 'ears', 'earlobe',
            'hair', 'hairline', 'jaw', 'jugular vein', 'chin', 'posterior', 'anus', 'eyebrow', 'lips', 'teeth', 'tooth', 'tongue',
            'temple', 'brain', 'breasts', 'nipple', 'breast']
  attack_method = ['ripped off', 'severed', 'impaled', 'smashed', 'stomped', 'blugeoned', 'destroyed', 'shredded',
                    'hacked off', 'inverted', 'cracked', 'shattered', 'grazed', 'brushed', 'scraped', 'stabbed', 'snapped',
                    'detached', 'loosened', 'knocked out', 'bruised', 'bloodied', 'tore out', 'bit', 'kicked', 'whacked', 'curbstomped',
                    'jumped on', 'smacked', 'twisted', 'exploded', 'fractured', 'tore', 'twisted', 'dislocated', 'punctured', 'perforated',
                    'flattened', 'squashed']

  for i in range(1, randint(2, 6)):
    #amount of attacks is random
    await client.say("%s has %s %s's %s." % (ctx.message.author.display_name, random.choice(attack_method), attacked_user, random.choice(organs)))

#add a dang prismatology thing

#redacted the invite link
@client.command(pass_context=True)
async def invite(ctx):
  await client.say("")
#figure out how to use to incorporate id for stuff

client.run("")
#nice try