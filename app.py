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
import asyncio
from urllib import request
import re
import os
import datetime
from time import sleep
import yippi
import aiorule34


Client = discord.Client
bot_prefix = '|'
client = commands.Bot(command_prefix=bot_prefix)
#serv = discord.client.Guild
#commented out it just causes errors with rewrite and heroku for some reason
'''
Todo:
add role assignment (dyno style)
pornhub thumbnails (on hold because pornhub is stupid)    
persistent variables
r34 lookup
'''

'''
deprecated things for possible later use
global prismatology
num = None
global num
prismatology = {}
'''

channel = discord.utils.get(client.get_all_channels(), name='general')
client.remove_command('help')
#replaces help command with proprietary one

#connects to discord through api and returns values
@client.event
async def on_ready():
  print('Initialized.')
  print('Logged in as')
  print(discord.version_info)
  print(client.user.name)
  print(client.user.id)
  print('------')
  game = discord.Game(name="say |help")
  await client.change_presence(status=discord.Status.online, activity=game)
#help message



#\ndef swearcheck(m):\n  f = \'asset/SwearWords.txt\'\n  message_dict = dict(channel_id=m.channel.id)\n  while not client.is_closed:\n    for i in m:\n      i in f.read() == True\n        \n\n@commands.check(swearcheck)\nasync def swearchecker(m):\n  await client.say("No s:b:earing this is a christian server")\n  \n'
#a theoretical swear checker that has been commented out

@client.command()
async def sup(ctx):
  print(ctx)
  await ctx.send('wassup fool?')
#basic way to see if the bot is alive

@client.command()
async def roll(ctx, num):
  a = (int(num) - int(num)) + 1
  await ctx.send('Roll from 1 to {}:'.format(num))
  await ctx.send(randint(a, int(num)))
  #dice function


@client.command()
async def purge(ctx, messagestopurge):
  try:  
    useflag = 0
    for role in ctx.message.author.roles: #checks all roles of user
      if str(role).lower() == "richardmod": #checks that the richardmod role is assigned to the user
        useflag = 1 #richardmod role is present
    if useflag == 1:
      messagestopurge = int(messagestopurge)
      await ctx.message.delete()
      if messagestopurge <= 31: 
        await ctx.message.channel.purge(limit = messagestopurge, bulk=True)
        await ctx.send("Purged %d messages." % (messagestopurge))
      elif messagestopurge > 31:
        await ctx.send("I can't purge over 30 messages in one command.")
    else:
      await ctx.send("You do not have permission to do this.\nTo use this function, Please give users you would like to let use the function the role `RichardMod`.")            
  except:
    await ctx.send("I either don't have permission to delete messages here, a message I attempted to purge was removed, or some other error occurred. Please give me the permissions to delete messages to use this command.")     


@client.command()
async def emojify(ctx, *, args):
  foo = []
  foo2 = []
  #foo2 is the final output
  for phrase in args:
    foo.append(phrase)
  foo = ''.join(foo)
  for phrase in foo.split():
    a = randint(0, 3)
    going_to = ['gonna', 'finna']
    #nword = ['ni:b::b:a', 'nigga']
    #who = ['whom', 'whomst', "whom'st", "whomst'd", "whom'st'd've", "whom'st'd", "whom'st'd've'll", "whom'stdve'll"]
    phrase = phrase.replace('motherfucker', 'mf')
    phrase = phrase.replace('motherfucking', 'mf')
    phrase = phrase.lower()
    phrase = phrase.replace('who')
    phrase = phrase.replace('b', ':b:')
    phrase = phrase.replace('nigga')
    phrase = phrase.replace('trying to', 'tryna')
    phrase = phrase.replace('right now', 'rn')
    phrase = phrase.replace('gonna', random.choice(going_to))
    phrase = phrase.replace('going to', random.choice(going_to))
    phrase = phrase.replace('that', 'dat')
    phrase = phrase.replace("you're", 'ur')
    phrase = phrase.replace('your', 'ur')
    #word replacement
    emojis = [
      ':joy:', ':100:', ':ok_hand:', ':eyes:', ':fire:', ':sweat_drops:', ':joy:', ':clap:', ':gun:',
      ':money_with_wings:', ':dollar:', ':sunglasses:', ':tongue:', ':wink:', ':eggplant:', ':muscle:',
      ':thinking:', ':triumph:', ':sunglasses:', ':cry:', ':sob:', ':wink:', ':smirk:', ':unamused:',':hugging:',
      ':rolling_eyes:',':expressionless:',':neutral_face:',':runner:',':tired_face:',':weary:',':dizzy_face:',':astonished:',
      ':rage:',':no_good:',':smiling_imp:',':joy_cat:',':face_palm:', ':full_moon_with_face:', ':new_moon_with_face:'
    ]
    if a <= 2:
      phrase = (phrase + ' ') + random.choice(emojis)
      foo2.append(phrase)
    else:
      foo2.append(phrase)
      pass
  if len(' '.join(foo2)   ) <= 2000:
    await ctx.send(' '.join(foo2))
    await ctx.message.delete()
  else:
    await ctx.send("Sorry, too long.")
    


@client.command()
async def joined_at(ctx, member: discord.Member = None):
  if member is None:
    member = ctx.author
  await ctx.send('{0} joined at {0.joined_at}'.format(member))
  #checks join date of user


@client.command()
async def calculator(ctx, a, b, c):
  a = list(a)
  for i in a:
    if not i.isnumeric() and not i == '.':
      a.remove(i)            
      a = ''.join(a)
  b = list(b)
  for i in b:
    if not i.isnumeric() and not i == '.':
      b.remove(i)
      b = ''.join(b)
  c = list(c)
  for i in c:
    if not i.isnumeric() and not i == '.':
      c.remove(i)
      c = ''.join(c)    
  o = '{} {} {} is {}'
  if b == '+':
    d = int(a) + int(c)
    o = o.format(a, b, c, d)
    await ctx.send(o)
  elif b == '-':
    d = int(a) - int(c)
    o = o.format(a, b, c, d)
    await ctx.send(o)
  elif (b == 'x') or (b == '*'):
    d = int(a) * int(c)
    o = o.format(a, b, c, d)
    await ctx.send(o)
  elif b == '/':
    d = float(a) / float(c)
    o = o.format(a, b, c, d)
    await ctx.send(o)


@client.command()
async def help(ctx):
  helpmessage = """\nHi, I'm Richardbot, and I can do things.\n
Command prefix, |, type | before commands\n
|purge x, purges messages, x being the number of messages to remove.
**NOTE: You must have the role `RichardMod` to use this function. Please give users you would like to let use the function the role.** \n
|mydong, shows your dong length.\n
|roll x, rolls a dice, type |roll and then the number of faces.\n
|nsfw, returns pornhub video on query (NSFW CHANNELS ONLY)\n
|emojify, replaces the letter b with :b:, adds emojis to your message.\n
|calculator a b c, does math. a is the first number, b is the operation, c is the second number.\n
|flip, flips a coin.\n
|eightball, gives you a virtual eightball fortune.\n
|say, richardbot repeats what you said.\n
|e621, enter a query and the bot will give you one of the first 30 results on e621. This bot uses 
the same sytnax as e621's search function, consult their cheatsheet here for syntax: https://e621.net/help/show/cheatsheet 
(NSFW CHANNELS ONLY)\n
|r34, searches on rule34.xxx based on query. Consult https://rule34.xxx/index.php?page=help and https://rule34.xxx/index.php?page=help&topic=cheatsheet.
(NSFW CHANNELS ONLY)\n
|ytsearch, gives the top youtube result based on search.\n
|invite, gives you an invite for richardbot.\n
|censor, censors what you said.\n
|joined\_at, prints when you joined.
\n
*This bot was created by Flammable.*
Twitter: @Flammabl3\_
Reddit: /u/Flammable\_
steam: https://steamcommunity.com/id/somethingsburning/
Discord: Flammable#7154"""
  await ctx.send(helpmessage)


@client.command()
async def flip(ctx):
  a = ctx.message.channel
  coinflip = randint(0, 2)
  if coinflip == 0:
    await ctx.send('Heads!')
    await a.send(file=discord.File('asset/heads.png', filename='asset/heads.png'))
  elif coinflip == 1:
    await ctx.send('Tails!')
    await a.send(file=discord.File('asset/tails.png', filename='asset/tails.png'))


@client.command()
async def eightball(ctx):
  answers = [
    'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
    'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
    'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
    "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
  ]
  await ctx.send(random.choice(answers))


@client.command()
async def say(ctx, *, phrase):
  full_phrase = []
  begin = ''.join(phrase)
  for i in begin.split():
    full_phrase.append(i)
  final = ' '.join(full_phrase)
  try:
    await ctx.message.delete()
  except:
    pass
  await ctx.send(final)
  #bot parrots user

"""
for phrase in args:
    foo.append(phrase)
  foo = ''.join(foo)
  for phrase in foo.split():
"""
@client.command()
async def ytsearch(ctx, *, args):
  try:
    query_list = []
    query2 = []
    for i in args:
      if not i.isalpha() and not i.isdigit():
         i.strip(i)
      i = i.lower()
      query_list.append(i)
    query_list = ''.join(query_list)
    for i in query_list.split():
      i += '+'
      query2.append(i)
    query2 = ''.join(query2)
    url = 'https://www.youtube.com/results?search_query={}'.format(query2)
    hdr = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36',
    }
    urlrequest = request.Request(url, headers=hdr)
    page = request.urlopen(urlrequest)
    search_results = re.findall('href=\\"\\/watch\\?v=(.{11})', page.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[1])
  except IndexError:
    await ctx.send("Sorry, no results.")

@client.command()
async def alexa(ctx, *, args):
  try:
    illegal_chars = ['<', '>', '#', '%', '{', '}', '|', '\\', '^',
             '~', '[', ']', '`', ';', '/', '?', ':', '@',
            '=', '&']
    query_list = []
    query2 = []
    for i in args:
      for char in illegal_chars:
        if char in i:
          i.strip(char)
      i = i.lower()
      if i != "play":
        query_list.append(i)
      if i == "play":
        continue
    query_list = ''.join(query_list)
    for i in query_list.split():
      i += '+'
      query2.append(i)
    query2 = ''.join(query2)
    url = 'https://www.youtube.com/results?search_query={}'.format(query2)
    hdr = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36',
    }
    urlrequest = request.Request(url, headers=hdr)
    page = request.urlopen(urlrequest)
    search_results = re.findall('href=\\"\\/watch\\?v=(.{11})', page.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[1])
  except IndexError:
    await ctx.send("Sorry, no results.")

"\n@client.command(pass_context=True)\nasync def indicator(ctx, *args):\n  b = []\n  for i in args:\n    if i == 'a':\n      i = ':regional_indicator_u:'\n      b.append(i)\n    if i == 'e':\n      i = ':regional_indicator_e:'\n      b.append(i)\n    if i == 'i':\n      i = ':regional_indicator_i:'\n      b.append(i)\n    if i == 'o':\n      i = ':regional_indicator_o:'\n      b.append(i)     \n    if i == 'u':\n      i = ':regional_indicator_u:'\n      b.append(i)\n    else:\n      b.append(i)\n    await client.say(''.join(b))\n"


@client.command()
async def censor(ctx, *, args):
  try:
    b = []
    for i in args:
      i = '█' * len(i)
      b.append(i)
    sleep(0.5)
    await ctx.message.delete()
    await ctx.send(''.join(b))
  except:
    await ctx.send("Error, probably missing delete permissions. Sorry.")


@client.command()
async def attack(ctx, *attacked):
  attacked_user = ' '.join(attacked)
  organs = [
    'big toe', 'toenail', 'pinky toe', 'toe', 'ankle', 'calf', 'knee', 'kneecap', 'thigh', 'radial artery', 'thigh',
    'femur', 'tibia', 'penis', 'testicles', 'scrotum', 'vagina', 'ovaries', 'intestines', 'spleen', 'stomach',
    'liver', 'kidneys', 'ribs', 'ribcage', 'heart', 'lungs', 'spine', 'tailbone', 'spinal cord', 'back', 'chest',
    'shoulder blade', 'arm', 'wrist', 'pinky', 'thumb', 'finger', 'shoulder', 'throat', 'trachea', 'esophagus',
    'eyeballs', 'nose', 'septum', 'frenulum', 'vulva', 'ears', 'earlobe', 'hair', 'hairline', 'jaw', 'jugular vein',
    'chin', 'posterior', 'anus', 'eyebrow', 'lips', 'teeth', 'tooth', 'tongue', 'temple', 'brain', 'breasts',
    'nipple', 'breast', 'forehead', 'bladder', 'gallblader', 'testicles'
  ]
  attack_method = [
    'ripped off', 'severed', 'impaled', 'smashed', 'stomped', 'blugeoned', 'destroyed', 'shredded', 'hacked off',
    'inverted', 'cracked', 'shattered', 'grazed', 'brushed', 'scraped', 'stabbed', 'snapped', 'detached',
    'loosened', 'knocked out', 'bruised', 'bloodied', 'tore out', 'bit', 'kicked', 'whacked', 'curbstomped',
    'jumped on', 'smacked', 'twisted', 'exploded', 'fractured', 'tore', 'twisted', 'dislocated', 'punctured',
    'perforated', 'flattened', 'squashed', 'pulverised'
  ]
  await ctx.send("%s has %s %s's %s." % (ctx.author.display_name, random.choice(attack_method), attacked_user,
                         random.choice(organs)))@client.command()

@client.command()
async def invite(ctx):
  await ctx.send('https://discordapp.com/oauth2/authorize?client_id=366038118136283136&scope=bot&permissions=121920')

client.run('')
#nice try