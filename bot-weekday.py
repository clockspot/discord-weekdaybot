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

client = discord.Client()

@client.event
async def on_ready():
  #print(f'{client.user} has connected to Discord!')
  
  #defaults
  from themes.default import weekdays as weekdaysDefault
  weekdays = False
  
  #potentially replace the above per date - also defines today
  from datelist.py import *
  
  for guild in client.guilds:
    #if str(guild.id) == GUILD: #do it for any that is connected
    for channel in guild.channels:
      if str(channel) == POSTCHAN:
        #In original usage, I had an array of weekday sets, and we would send the current weekday determined by ISO week % number of sets (last appeared in commit f89d7dd 2021-09-12)
        #Now we import per dates above
        if not weekdays: #if doing default weekday, send a random one
          await channel.send(random.choice(weekdaysDefault[today.weekday()]))
        else: #send the first one - let the rest (if any) come as responses to bot.py
          await channel.send(weekdays[today.weekday()])
  await client.close()

client.run(TOKEN)