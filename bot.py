# bot.py
import os
import random
from datetime import date

import discord
from dotenv import load_dotenv

genericResponses = [
  "https://tenor.com/view/happy-dancing-celebrate-excited-gif-13870839", #carltondance
  "https://tenor.com/view/will-ferrell-anchorman-glass-case-emotion-gif-5791193", #glass case of emotion
  "https://tenor.com/view/couple-burger-you-taste-like-a-burger-i-dont-like-you-anymore-gif-17016151",
  "https://tenor.com/view/jack-sparrow-i-wash-my-hands-of-this-weirdness-potc-wtf-weird-gif-11263756",
  "https://tenor.com/view/the-big-lebowski-jeff-bridges-the-dude-i-cant-be-worried-about-shit-life-goes-on-gif-4513832",
  "https://tenor.com/view/frankly-my-dear-i-dont-give-a-damn-idgaf-gif-18386670",
  "https://tenor.com/view/taxi-driver-you-talking-to-me-is-it-me-me-gif-16109534",
  "https://tenor.com/view/cool-b99-brooklyn-nine-nine-andy-samberg-detective-jake-peralta-gif-11062927",
  "https://tenor.com/view/anchorman-what-what-did-you-say-gif-13930968",
  "https://tenor.com/view/steve-brule-okay-ok-gif-11799872",
  "https://tenor.com/view/huh-confused-dont-know-thinking-john-c-reilly-gif-16141237",
  "https://tenor.com/view/steve-brule-shrug-surprised-gif-11799934",
]

languageResponses = [
  "https://tenor.com/view/your-language-is-offensive-watch-your-mouth-zach-galifianakis-gif-13885320",
  "https://tenor.com/view/funny-or-die-will-ferrell-watch-your-mouth-filthy-mouth-mouth-gif-4427315",
  "https://tenor.com/view/captain-america-marvel-avengers-gif-14328153",
  "https://tenor.com/view/scandal-scandalous-wink-cat-shocked-gif-15502893"
]

whoResponses = [
  "https://cdn.discordapp.com/attachments/855962058728931360/856205995276369930/hal.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856206275334766622/wopr.gif",
]

weekdays = [
  [ #MONDAY
    "monday",
    "https://tenor.com/view/blessings-god-bless-family-sparkle-monday-blessings-gif-16731080",
    "https://tenor.com/view/monday-cat-gif-8674980",
    "https://tenor.com/view/monday-its-monday-when-monday-hits-monday-morning-gm-gif-14243228"
  ],
  [ #TUESDAY
    "tuesday",
    "https://tenor.com/view/happy-tuesday-cookie-monster-dance-bert-and-ernie-dancing-sesame-street-gif-11719686",
    "https://tenor.com/view/its-only-tuesday-betty-white-faint-golden-girls-gif-11651875",
    "https://tenor.com/view/tuesdays-here-funny-animals-dog-roomba-gif-11713521"
  ],
  [ #WEDNESDAY
    "wensday",
    "wednesday",
    "https://tenor.com/view/wednesday-dance-celebrate-happy-wednesday-gif-10812164",
    "https://tenor.com/view/tee-tess-morning-good-blessings-gif-18801330",
    "https://tenor.com/view/yay-wednesday-yay-wednesday-happy-wednesday-happy-dance-gif-13946864"
  ],
  [ #THURSDAY
    "thursday",
    "https://tenor.com/view/thursday-happy-thursday-unicorn-dragging-rainbow-gif-15254014",
    "https://tenor.com/view/thursday-confetti-happy-thursday-celebrate-gif-11705413",
    "https://tenor.com/view/thursday-friday-funny-when-you-thought-its-fridayn-its-only-thursday-gif-15583680"
  ],
  [ #FRIDAY
    "friday",
    "https://tenor.com/view/nicolas-cage-friday-feel-that-friday-feeling-feel-that-thats-friday-gif-12235300",
    "https://tenor.com/view/time-to-do-friday-dance-cat-kittens-dancing-dance-moves-gif-16362746",
    "https://tenor.com/view/ant-man-when-its-friday-excited-tgif-gif-11962947"
  ],
  [ #SATURDAY
    "SATURDAY",
    "https://tenor.com/view/yeah-baby-funny-oh-yeah-its-saturday-gif-15025789",
    "https://tenor.com/view/svaradiofm-happy-saturday-make-the-most-of-this-day-laugh-love-read-just-be-happy-gif-15042816",
    "https://tenor.com/view/hello-top-of-the-morning-top-hat-cat-cheerio-gif-13926359"
  ],
  [ #SUNDAY
    "sunday",
    "https://tenor.com/view/lovely-sunday-have-a-good-day-flowers-butterfly-gif-8661074",
    "https://tenor.com/view/sunday-gif-10898789",
    "https://tenor.com/view/peaceful-have-a-blessed-sunday-sunday-blessed-gif-14992878"
  ]
]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  today = date.today()
  if message.author == client.user:
    return
  if client.user.mentioned_in(message):
    if "fuck" in message.content or "shit" in message.content:
      await message.channel.send(random.choice(languageResponses))
    elif "who" in message.content:
      await message.channel.send(random.choice(whoResponses))
    elif "day" in message.content or "date" in message.content:
      await message.channel.send(random.choice(weekdays[today.weekday()]))
    else:
      await message.channel.send(random.choice(genericResponses))
    return

client.run(TOKEN)
