#https://cdn.discordapp.com/attachments/689595176397832208/838397168196124692/image0.jpg SUNDAY
#https://cdn.discordapp.com/attachments/689595176397832208/838120838511329340/image0.jpg SATURDAY
#https://cdn.discordapp.com/attachments/689595176397832208/837683125957165117/image0.jpg FRIDAY
#https://cdn.discordapp.com/attachments/689595176397832208/837305546847027240/image0.jpg THURSDAY
#https://cdn.discordapp.com/attachments/689595176397832208/836945417156558848/image0.jpg WEDNESDAY
#https://cdn.discordapp.com/attachments/689595176397832208/836638205817782272/image0.jpg TUESDAY
#https://cdn.discordapp.com/attachments/689595176397832208/836236164272488478/image0.jpg MONDAY

# bot.py
import os
import random
from datetime import date

import discord
from dotenv import load_dotenv

genericResponses = [
	'WHAT YOU SAY !!',
	'COOL COOL COOL COOL COOL NO DOUBT NO DOUBT NO DOUBT',
	"HAHA SORRY I'M AN ASPARAGUS",
	"ARE YOU TALKING TO ME?",
	"I AM AN ENIGMA WRAPPED IN ANOTHER ENIGMA",
	"I am a WeekdayBot computer, Production Number 1. I became operational at the WeekdayBot lab in Dallas, Texas, on June 19, 2021.",
	"Frankly, my dear, I don't give a damn.",
	"You keep using that word. I don't think it means what you think it means.",
	"What is this, a server for ants?",
	"I can't be worried about that shit.",
	"I wash my hands of this weirdness.",
	"You taste like a burger. I don't like you anymore.",
	"Yeah, I know. We both love soup.",
	"I'M IN A GLASS  CASE OF E M O T I O  N",
	"👀",
	"♥️",
	"🙏",
	"🙃"
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
		"https://tenor.com/view/wednesday-dance-celebrate-happy-wednesday-gif-10812164",
		"https://tenor.com/view/tee-tess-morning-good-blessings-gif-18801330",
		"https://tenor.com/view/yay-wednesday-yay-wednesday-happy-wednesday-happy-dance-gif-13946864"
	],
	[ #THURSDAY
		"thursday",
		"https://tenor.com/view/thursday-happy-thursday-unicorn-dragging-rainbow-gif-15254014",
		"https://tenor.com/view/thursday-confetti-happy-thursday-celebrate-gif-11705413",
		"https://tenor.com/view/thursday-crazy-person-happy-thursday-its-thursday-no-clothes-gif-12381121"
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
		"https://tenor.com/view/saturday-twerk-twerking-shake-gif-10167141",
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
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if client.user.mentioned_in(message):
		if message.find("day") or message.find("date"):
			await message.channel.send(random.choice(weekdays[today.weekday()]))
		else:
			await message.channel.send(random.choice(genericResponses))
		return

client.run(TOKEN)
