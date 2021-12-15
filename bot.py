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
import themes.christmas1
import themes.christmas2
import themes.christmas3

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if client.user.mentioned_in(message):
    today = date.today()
    #themes, part 2 (see part 1)
    if today >= date(2022,1,3):
      theme = themes.default
    else if today >= date(2021,12,27):
      theme = themes.christmas3
    else if today >= date(2021,12,20):  
      theme = themes.christmas2
    else:
      theme = themes.christmas1
    
    if theme.languageResponses and ("fuck" in message.content or "f*ck" in message.content or "Fuck" in message.content or "FUCK" in message.content or "shit" in message.content or "Shit" in message.content or "SHIT" in message.content or "arse" in message.content or " ass" in message.content):
      await message.channel.send(random.choice(theme.languageResponses))
    elif theme.whoResponses and ("who" in message.content):
      await message.channel.send(random.choice(theme.whoResponses))
    elif "day" in message.content or "date" in message.content:
      if theme.weekdayLabels and theme.weekdayLabels[today.weekday()]: #for weeks where the gif doesn't explicitly say the weekday
        await message.channel.send(theme.weekdayLabels[today.weekday()]);
      await message.channel.send(random.choice(theme.weekdays[today.weekday()]))
    else:
      if theme.genericResponses:
        await message.channel.send(random.choice(theme.genericResponses))
      else:
        await message.channel.send(random.choice(themes.default.genericResponses))
    return

client.run(TOKEN)
