# bot-weekday.py
import os
import random
from datetime import date

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
POSTCHAN = os.getenv('DISCORD_POSTCHANNELNAME')

#themes, part 1 (see part 2, and also bot.py)
import themes.default
import themes.signlanguage

client = discord.Client()

@client.event
async def on_ready():
  #print(f'{client.user} has connected to Discord!')
  
  for guild in client.guilds:
    #if str(guild.id) == GUILD: #do it for any that is connected
    for channel in guild.channels:
      if str(channel) == POSTCHAN:
        today = date.today()
        #In original usage, I had an array of weekday sets, and we would send the current weekday determined by ISO week % number of sets (last appeared in commit f89d7dd 2021-09-12)
        #themes, part 2 (see part 1)
        if today >= date(2022,1,17):
          theme = themes.default
        else:
          theme = themes.signlanguage
          
        if theme.weekdayLabels and theme.weekdayLabels[today.weekday()]: #for weeks where the gif doesn't explicitly say the weekday
          await channel.send(theme.weekdayLabels[today.weekday()]);
          
        if theme.weekdays: #if theme specifies weekdays, send the first – any others can come as responses to bot.py
          await channel.send(theme.weekdays[today.weekday()][0])
        else: #if theme doesn't specify weekdays, send a random one from default theme
          await channel.send(random.choice(themes.default.weekdays[today.weekday()]))
          
  await client.close()

client.run(TOKEN)