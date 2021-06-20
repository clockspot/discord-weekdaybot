#https://cdn.discordapp.com/attachments/689595176397832208/838397168196124692/image0.jpg SUNDAY
#https://cdn.discordapp.com/attachments/689595176397832208/838120838511329340/image0.jpg SATURDAY
#https://cdn.discordapp.com/attachments/689595176397832208/837683125957165117/image0.jpg FRIDAY
#https://cdn.discordapp.com/attachments/689595176397832208/837305546847027240/image0.jpg THURSDAY
#https://cdn.discordapp.com/attachments/689595176397832208/836945417156558848/image0.jpg WEDNESDAY
#https://cdn.discordapp.com/attachments/689595176397832208/836638205817782272/image0.jpg TUESDAY
#https://cdn.discordapp.com/attachments/689595176397832208/836236164272488478/image0.jpg MONDAY

# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(f'Connected to {guild.name} ({guild.id})')
        if str(guild.id) == GUILD:
            print(f"This is the one we're interested in")
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}')
            break

client.run(TOKEN)