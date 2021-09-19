# bot.py
import os
import random
from datetime import date

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  #defaults
  from themes.default import genericResponses, weekdays
  languageResponses = False
  whoResponses = False
  
  #potentially replace the above per date - also defines today
  from datelist.py import *
  
  if client.user.mentioned_in(message):
    if languageResponses and ("fuck" in message.content or "shit" in message.content or "arse" in message.content or "ass" in message.content):
      await message.channel.send(random.choice(languageResponses))
    elif whoResponses and ("who" in message.content):
      await message.channel.send(random.choice(whoResponses))
    elif "day" in message.content or "date" in message.content:
      await message.channel.send(random.choice(weekdays[today.weekday()]))
    else:
      await message.channel.send(random.choice(genericResponses))
    return

client.run(TOKEN)
