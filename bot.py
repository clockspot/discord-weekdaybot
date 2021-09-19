# bot.py
import os
import random
from datetime import date

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#themes, part 1 (see part 2, and also bot-weekday.py)
import themes.default
import themes.french
import themes.niccage1
import themes.niccage2
import themes.niccage3

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if client.user.mentioned_in(message):
    
    #themes, part 2 (see part 1)
    theme = themes.default
    #if today >= date(2021,10,11): #birthday campout 10/15-17
      #theme = themes.joebob
    if today >= date(2021,10,4):
      theme = themes.niccage3
    elif today >= date(2021,9,27):
      theme = themes.niccage2
    elif today >= date(2021,9,20):
      theme = themes.niccage1
    elif today >= date(2021,9,13): #ann's bday 9/14
      theme = themes.french
    else:
      theme = themes.default
    
    if theme.languageResponses and ("fuck" in message.content or "f*ck" in message.content or "Fuck" in message.content or "FUCK" in message.content or "shit" in message.content or "Shit" in messgae.content or "SHIT" in message.content or "arse" in message.content or " ass" in message.content):
      await message.channel.send(random.choice(theme.languageResponses))
    elif theme.whoResponses and ("who" in message.content):
      await message.channel.send(random.choice(theme.whoResponses))
    elif "day" in message.content or "date" in message.content:
      today = date.today()
      await message.channel.send(random.choice(theme.weekdays[today.weekday()]))
    else:
      if theme.genericResponses:
        await message.channel.send(random.choice(theme.genericResponses))
      else:
        await message.channel.send(random.choice(themes.default.genericResponses))
    return

client.run(TOKEN)
