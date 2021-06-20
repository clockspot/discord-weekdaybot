# bot-weekday.py
import os
#import random
from datetime import date

import discord
from dotenv import load_dotenv

#weekdays in Python are 0=Monday
weekdaysNancy = [
  "https://cdn.discordapp.com/attachments/689595176397832208/836236164272488478/image0.jpg", #MONDAY
  "https://cdn.discordapp.com/attachments/689595176397832208/836638205817782272/image0.jpg", #TUESDAY
  "https://cdn.discordapp.com/attachments/689595176397832208/836945417156558848/image0.jpg", #WEDNESDAY
  "https://cdn.discordapp.com/attachments/689595176397832208/837305546847027240/image0.jpg", #THURSDAY
  "https://cdn.discordapp.com/attachments/689595176397832208/837683125957165117/image0.jpg", #FRIDAY
  "https://cdn.discordapp.com/attachments/689595176397832208/838120838511329340/image0.jpg", #SATURDAY
  "https://cdn.discordapp.com/attachments/689595176397832208/838397168196124692/image0.jpg", #SUNDAY
]

weekdaysStrip = [
  "https://cdn.discordapp.com/attachments/855962058728931360/856023151263481876/guy-mon.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856023273988423680/guy-tue.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856023359267274762/guy-wed.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856023425985413131/guy-thu.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856023504856154112/guy-fri.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856023710896750632/guy-sat.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856023770267254794/guy-sun.gif"
]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
POSTCHAN = os.getenv('DISCORD_POSTCHANNELNAME')

client = discord.Client()

@client.event
async def on_ready():
  #print(f'{client.user} has connected to Discord!')
  today = date.today()
  for guild in client.guilds:
    #if str(guild.id) == GUILD: #do it for any that is connected
    for channel in guild.channels:
      if str(channel) == POSTCHAN:
        await channel.send(weekdaysNancy[today.weekday()])
        await client.close()

client.run(TOKEN)