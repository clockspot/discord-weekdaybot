# bot-weekday.py
import os
#import random
from datetime import date

import discord
from dotenv import load_dotenv

#weekdays in Python are 0=Monday
#the particular set of weekdays returned for this week is determined by ISO week % number of weekday sets
#there is usually a big reveal on Sunday, the last day of the ISO week
weekdays = [
  [ #nancy
    "https://cdn.discordapp.com/attachments/689595176397832208/836236164272488478/image0.jpg", #MONDAY
    "https://cdn.discordapp.com/attachments/689595176397832208/836638205817782272/image0.jpg", #TUESDAY
    "https://cdn.discordapp.com/attachments/689595176397832208/836945417156558848/image0.jpg", #WEDNESDAY
    "https://cdn.discordapp.com/attachments/689595176397832208/837305546847027240/image0.jpg", #THURSDAY
    "https://cdn.discordapp.com/attachments/689595176397832208/837683125957165117/image0.jpg", #FRIDAY
    "https://cdn.discordapp.com/attachments/689595176397832208/838120838511329340/image0.jpg", #SATURDAY
    "https://cdn.discordapp.com/attachments/689595176397832208/838397168196124692/image0.jpg", #SUNDAY
  ],
  [ #mutts today's the day
    "https://cdn.discordapp.com/attachments/855962058728931360/856545968097591296/ttd-mon.jpg",
    "https://cdn.discordapp.com/attachments/855962058728931360/856546058406723584/ttd-tue.jpg",
    "https://cdn.discordapp.com/attachments/855962058728931360/856546093756055572/ttd-wed.jpg",
    "https://cdn.discordapp.com/attachments/855962058728931360/856546126715289660/ttd-thu.jpg",
    "https://cdn.discordapp.com/attachments/855962058728931360/856546161221435412/ttd-fri.jpg",
    "https://cdn.discordapp.com/attachments/855962058728931360/856546190326104084/ttd-sat.jpg",
    "https://cdn.discordapp.com/attachments/855962058728931360/856546218536206336/ttd-sun.jpg",
  ],
  [ #sign language
    "https://cdn.discordapp.com/attachments/855962058728931360/856547401233203260/source-1.gif", #mon
    "https://cdn.discordapp.com/attachments/855962058728931360/856547484847702056/5c2dd13b01a59f138c2a9a427d53a858.gif", #tue
    "https://cdn.discordapp.com/attachments/855962058728931360/856547685455495198/giphy.gif", #wed (every?)
    "https://cdn.discordapp.com/attachments/855962058728931360/856547786279354368/7QsG.gif", #thu
    "https://cdn.discordapp.com/attachments/855962058728931360/856547899441545226/5fa539ebbdd03928df011188e16b47a1.gif", #fri
    "https://cdn.discordapp.com/attachments/855962058728931360/856547985818517594/source-2.gif", #sat (weekend)
    "https://cdn.discordapp.com/attachments/855962058728931360/856548072094695444/4af91bf76cfacb7e6ead7428c502adef.gif", #sun
  ],
  [ #stripper guy
    "https://cdn.discordapp.com/attachments/855962058728931360/856023151263481876/guy-mon.gif",
    "https://cdn.discordapp.com/attachments/855962058728931360/856023273988423680/guy-tue.gif",
    "https://cdn.discordapp.com/attachments/855962058728931360/856023359267274762/guy-wed.gif",
    "https://cdn.discordapp.com/attachments/855962058728931360/856023425985413131/guy-thu.gif",
    "https://cdn.discordapp.com/attachments/855962058728931360/856023504856154112/guy-fri.gif",
    "https://cdn.discordapp.com/attachments/855962058728931360/856023710896750632/guy-sat.gif",
    "https://cdn.discordapp.com/attachments/855962058728931360/856023770267254794/guy-sun.gif"
  ],
  [ #office cat gifs
    "https://cdn.discordapp.com/attachments/855962058728931360/856548197768757278/7t6o.gif", #mon
    "https://cdn.discordapp.com/attachments/855962058728931360/856548519473315870/tenor.gif", #tue
    "https://cdn.discordapp.com/attachments/855962058728931360/856548641346551818/c7fe2ff8ea711c83a70cb400bfd8b1ab.gif", #wed
    "https://cdn.discordapp.com/attachments/855962058728931360/856548739798663188/source.gif", #thu
    "https://cdn.discordapp.com/attachments/855962058728931360/856548843658674176/7t6q.gif", #fri
    "https://cdn.discordapp.com/attachments/855962058728931360/856549233926078495/giphy-1.gif", #sat
    "https://cdn.discordapp.com/attachments/855962058728931360/856549797984731136/happy-sunday-cats.jpg", #sun
  ],
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
        #send the current weekday from the set of weekdays determined by current ISO week
        await channel.send(weekdays[today.isocalendar()[1]%len(weekdays)][today.weekday()])
  await client.close()

client.run(TOKEN)