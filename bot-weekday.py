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
  [ #sparkle blessings
    "https://tenor.com/view/blessings-god-bless-family-sparkle-monday-blessings-gif-16731080", #mon
    "https://tenor.com/view/tuesday-typical-tuesday-another-tuesday-elmo-tuesday-potty-elmo-tuesday-gif-21048101", #tue
    "https://tenor.com/view/tee-tess-morning-good-blessings-gif-18801330", #wed
    "https://c.tenor.com/DPVIwmxEmgYAAAAC/happy-thursday.gif", #thu
    "https://c.tenor.com/ldnhJe8zeBUAAAAC/jumma-mubarak-good-morning.gif", #fri
    "https://tenor.com/view/svaradiofm-happy-saturday-make-the-most-of-this-day-laugh-love-read-just-be-happy-gif-15042816", #sat
    "https://tenor.com/view/lovely-sunday-have-a-good-day-flowers-butterfly-gif-8661074", #sun
  ],
  [ #itysl guy
    "https://c.tenor.com/xO1tDRNiYI4AAAAC/stinky-fart.gif",
    "https://c.tenor.com/9H0xDgUjUR4AAAAC/toast-dead.gif",
    "https://c.tenor.com/T6DRX77UpSgAAAAC/focus-group-oh-nice.gif",
    "https://c.tenor.com/-w2DeZAuzQEAAAAC/focus-group-admit-it.gif",
    "https://c.tenor.com/t4LTqvGNTGUAAAAC/good-idea-i-stand-by-it.gif",
    "https://c.tenor.com/H4f-WMRVeAsAAAAC/im-doing-the-best-im-the-best.gif",
    "https://c.tenor.com/hAdOE2zI1EEAAAAC/shut-up-paul-i-think-you-should-leave.gif"
  ],
  [ #cats
    "https://tenor.com/view/monday-oh-hell-its-monday-kitten-gif-12614221", #mon
    "https://c.tenor.com/DYhRqMQu5cUAAAAC/cat-typing.gif", #tue
    "https://tenor.com/view/yay-wednesday-yay-wednesday-happy-wednesday-happy-dance-gif-13946864", #wed
    "https://tenor.com/view/thursday-friday-funny-when-you-thought-its-fridayn-its-only-thursday-gif-15583680", #thu
    "https://tenor.com/view/purrfect-its-friday-cat-kitten-kitty-gif-16398687", #fri
    "https://tenor.com/view/hello-top-of-the-morning-top-hat-cat-cheerio-gif-13926359", #sat
    "https://c.tenor.com/GmAjGttBWjIAAAAC/cat-kitten.gif", #sun
  ],
  [ #random
    "https://tenor.com/view/monday-its-monday-when-monday-hits-monday-morning-gm-gif-14243228", #kid runs into wall
    "https://cdn.discordapp.com/attachments/855980303570042910/874152902569115648/1a2f1f5c9da70b147b7c8fba1435a15b.gif", #on a tuesday in space
    "https://cdn.discordapp.com/attachments/855980303570042910/874153351640653824/giphy-4.gif", #wacky wednesday bubbles guy
    "https://cdn.discordapp.com/attachments/855980303570042910/874153923403989022/giphy-5.gif", #data high five
    "https://cdn.discordapp.com/attachments/855980303570042910/874154726994886707/giphy-7.gif", #surfing grandma
    "https://tenor.com/view/saturday-dance-old-dancing-party-hard-gif-11712974", #grandma in the kitchen with friends
    "https://c.tenor.com/jNlvxznV_6cAAAAd/happy-funday-sunday.gif", #reverse mimosa
  ],
]

weekdayNames = [
  "monday",
  "tuesday",
  "wednesday",
  "thursday",
  "friday",
  "saturday",
  "sunday"
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
        if(today.isocalendar()[1]%len(weekdays)==6):
          await channel.send(weekdayNames[today.weekday()])
        await channel.send(weekdays[today.isocalendar()[1]%len(weekdays)][today.weekday()])
  await client.close()

client.run(TOKEN)