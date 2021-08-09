# bot.py
import os
import random
from datetime import date

import discord
from dotenv import load_dotenv

genericResponsesOld = [
  "https://tenor.com/view/happy-dancing-celebrate-excited-gif-13870839", #carltondance
  #"https://tenor.com/view/will-ferrell-anchorman-glass-case-emotion-gif-5791193", #glass case of emotion
  "https://tenor.com/view/couple-burger-you-taste-like-a-burger-i-dont-like-you-anymore-gif-17016151",
  #"https://tenor.com/view/jack-sparrow-i-wash-my-hands-of-this-weirdness-potc-wtf-weird-gif-11263756",
  "https://tenor.com/view/the-big-lebowski-jeff-bridges-the-dude-i-cant-be-worried-about-shit-life-goes-on-gif-4513832",
  "https://tenor.com/view/frankly-my-dear-i-dont-give-a-damn-idgaf-gif-18386670",
  "https://tenor.com/view/taxi-driver-you-talking-to-me-is-it-me-me-gif-16109534",
  #"https://tenor.com/view/cool-b99-brooklyn-nine-nine-andy-samberg-detective-jake-peralta-gif-11062927",
  #"https://tenor.com/view/anchorman-what-what-did-you-say-gif-13930968",
  "https://tenor.com/view/steve-brule-okay-ok-gif-11799872",
  "https://tenor.com/view/huh-confused-dont-know-thinking-john-c-reilly-gif-16141237",
  "https://tenor.com/view/steve-brule-shrug-surprised-gif-11799934",
  "https://tenor.com/view/stfu-i-dont-care-ned-flanders-gif-18152062",
  "https://tenor.com/view/gifminster-matt-hancock-hancock-laughing-laughing-hysterically-gif-17657084",
  "https://tenor.com/view/awkward-nod-okay-then-uncomfortable-gif-10597719",
  "https://tenor.com/view/sure-thing-ok-whatever-uhhuh-gif-3871592",
  "https://tenor.com/view/kazoo-kid-wow-amazed-awkward-looking-gif-5484661",
  "https://tenor.com/view/funny-silly-wtf-crazy-kitty-gif-12896137",
  "https://tenor.com/view/star-trek-data-shrug-what-no-idea-gif-13886831",
]

genericResponses = [
  #"https://c.tenor.com/z6HsOw58c4wAAAAC/paul-rudd-shiit.gif",
  "https://c.tenor.com/k4HLyTN-2KIAAAAC/paul-rudd-eyebrow-raise.gif",
  #"https://c.tenor.com/he0KLHEhAOoAAAAC/who-wouldve-thought-not-me.gif",
  "https://c.tenor.com/AxpRazK7uksAAAAC/paul-rudd-nod.gif",
  "https://c.tenor.com/SqG9ga76ZLcAAAAC/tayne-nude-tayne.gif",
  "https://c.tenor.com/axm9sSdbTYAAAAAC/celeryman-intro.gif",
  "https://c.tenor.com/UUXPUkiIk8MAAAAd/paul-rudd-oh-no.gif",
  "https://c.tenor.com/c4JGCg4b8GEAAAAC/paul-rudd.gif",
  "https://c.tenor.com/cm9E2QnR17kAAAAd/paul-rudd-annoyed.gif",
  "https://c.tenor.com/9dkWhzNz_-IAAAAC/whatever-paul-rudd.gif",
  "https://c.tenor.com/PzD4WkywmZkAAAAC/paul-rudd-you.gif",
  "https://c.tenor.com/_036Vh7aca4AAAAC/marvel-antman-and-the-wasp.gif",
  "https://c.tenor.com/WGFxHlrjjFsAAAAC/clueless-paul-rudd.gif",
  "https://c.tenor.com/VBU8bHt3n-EAAAAC/paul-rudd-cool.gif",
  "https://c.tenor.com/Y8V_5QYpY3MAAAAC/paul-rudd-smiling.gif",
  "https://c.tenor.com/BgQIt6neBHMAAAAd/paul-rudd-deal-with-it.gif",
  "https://c.tenor.com/M_Hdbq1CergAAAAC/paul-rudd-y-fronts.gif",
]

itysl = [
  "https://c.tenor.com/zh7nN3zhlXMAAAAC/shut-up-paul-i-think-you-should-leave.gif",
  "https://c.tenor.com/b-291TsIh3EAAAAC/tim-robinson-i-think-you-should-leave.gif", #you sure about that
  "https://c.tenor.com/mUmjFyiLT5IAAAAC/hat-itysl.gif",
  "https://c.tenor.com/gZc8yab1QjgAAAAC/pointing-man-in-diner.gif",
  "https://c.tenor.com/8GJicVMU5FQAAAAC/what-wtf.gif",
  "https://c.tenor.com/wcwIn1E5k2cAAAAd/i-think-you-should-leave-tim-robinson.gif",
  "https://c.tenor.com/0fo9V99YtH4AAAAC/ahhh-i-think-you-should-leave-with-tim-robinson.gif",
  "https://c.tenor.com/ybXjC_4mpMkAAAAd/itysl-whattheheck.gif",
  "https://c.tenor.com/T6DRX77UpSgAAAAC/focus-group-oh-nice.gif",
  "https://c.tenor.com/hAdOE2zI1EEAAAAC/shut-up-paul-i-think-you-should-leave.gif",
  "https://c.tenor.com/srAfREAWwJIAAAAC/stare-i-think-you-should-leave.gif",
  "https://c.tenor.com/hkNb-P8hb_sAAAAd/i-think-you-should-leave.gif",
  "https://c.tenor.com/rb3YBTds_RcAAAAC/itysl-i-think-you-should-leave.gif",
  "https://c.tenor.com/IRXQni1lHxgAAAAd/karl-havoc.gif",
  "https://c.tenor.com/9hYw__gUrhkAAAAC/wrong-incorrect.gif",
  "https://c.tenor.com/I3xOvPhVq-kAAAAC/random-itysl.gif",
  "https://c.tenor.com/x-TOXtmgsCgAAAAd/tim-tim-robinson.gif",
  #"https://c.tenor.com/qqHH5NeIeK8AAAAC/bones-equal-dollars-tim-robinson.gif",
]

languageResponses = [
  "https://c.tenor.com/z6HsOw58c4wAAAAC/paul-rudd-shiit.gif",
  "https://c.tenor.com/b9kJkNjYbV8AAAAC/paul-paulrudd.gif",
  # "https://tenor.com/view/your-language-is-offensive-watch-your-mouth-zach-galifianakis-gif-13885320",
  # "https://tenor.com/view/funny-or-die-will-ferrell-watch-your-mouth-filthy-mouth-mouth-gif-4427315",
  # "https://tenor.com/view/captain-america-marvel-avengers-gif-14328153",
  # "https://tenor.com/view/scandal-scandalous-wink-cat-shocked-gif-15502893",
  # "https://tenor.com/view/fuck-you-no-elton-john-gif-12191991",
  
  #itysl
  #"https://c.tenor.com/QKKbKED9PmcAAAAC/dont-swear-swear.gif",
  #"https://c.tenor.com/SPC_2svCnQIAAAAC/pice-of-shit-pos.gif",
  #"https://c.tenor.com/zh7nN3zhlXMAAAAC/shut-up-paul-i-think-you-should-leave.gif",
  #"https://c.tenor.com/u0y_mjZMm2sAAAAC/come-here-little-fuck.gif"
]

whoResponses = [
  #"https://c.tenor.com/Vv2tv9E50AIAAAAC/i-cannot-talk-about-it-i-think-you-should-leave-with-tim-robinson.gif",

  "https://cdn.discordapp.com/attachments/855962058728931360/856205995276369930/hal.gif",
  "https://cdn.discordapp.com/attachments/855962058728931360/856206275334766622/wopr.gif",
  "https://tenor.com/view/computer-probloms-gif-18129019",
  "https://tenor.com/view/1984-movie-projector-gif-8163423",
  "https://tenor.com/view/star-trek-data-shrug-what-no-idea-gif-13886831",
]

weekdays = [
  [ #MONDAY
    "monday",
    "https://tenor.com/view/blessings-god-bless-family-sparkle-monday-blessings-gif-16731080",
    "https://tenor.com/view/monday-cat-gif-8674980", #monday cat fall over by wall
    "https://tenor.com/view/monday-its-monday-when-monday-hits-monday-morning-gm-gif-14243228", #kid runs into wall
    "https://tenor.com/view/monday-oh-hell-its-monday-kitten-gif-12614221", #oh hell it's monday cat
    "https://tenor.com/view/puppy-high-five-give-me-five-five-pet-gif-19385201", #happy monday high five small white dog
    "https://cdn.discordapp.com/attachments/855980303570042910/874151437767168000/giphy.gif", #ugh mondays exhausted girl
    "https://cdn.discordapp.com/attachments/855980303570042910/874152052379512842/e51834beb7c58977f5df235f5d2028ba.gif" #snl chris kattan?
    "https://cdn.discordapp.com/attachments/855980303570042910/874152189256405012/giphy-1.gif", #kid spray water in face
  ],
  [ #TUESDAY
    "tuesday",
    "https://tenor.com/view/happy-tuesday-cookie-monster-dance-bert-and-ernie-dancing-sesame-street-gif-11719686",
    "https://tenor.com/view/its-only-tuesday-betty-white-faint-golden-girls-gif-11651875",
    "https://tenor.com/view/tuesdays-here-funny-animals-dog-roomba-gif-11713521",
    "https://tenor.com/view/two-for-tuesday-tuesday-drinks-2for-tuesday-gif-15066898",
    "https://tenor.com/view/tuesday-typical-tuesday-another-tuesday-elmo-tuesday-potty-elmo-tuesday-gif-21048101", #blessed
    "https://cdn.discordapp.com/attachments/855980303570042910/874152267031379988/giphy-2.gif", #diabeetus throw stuff off desk
    "https://cdn.discordapp.com/attachments/855980303570042910/874152730711711754/giphy-3.gif", #tuesday mood lady eats sandwich through computer
    "https://cdn.discordapp.com/attachments/855980303570042910/874152815977705602/200w.gif", #hap pee tuse day
    "https://cdn.discordapp.com/attachments/855980303570042910/874152902569115648/1a2f1f5c9da70b147b7c8fba1435a15b.gif", #on a tuesday in space
    "https://c.tenor.com/DYhRqMQu5cUAAAAC/cat-typing.gif", #fast type cat
  ],
  [ #WEDNESDAY
    "wensday",
    "wednesday",
    "https://tenor.com/view/wednesday-dance-celebrate-happy-wednesday-gif-10812164", #wednesday addams
    "https://tenor.com/view/tee-tess-morning-good-blessings-gif-18801330", #love peace and happiness sparkles
    "https://tenor.com/view/yay-wednesday-yay-wednesday-happy-wednesday-happy-dance-gif-13946864", #dancing cat
    "https://tenor.com/view/smile-good-morning-wednesday-coffee-sparole-gif-13536158", #love u
    "https://tenor.com/view/wednesday-hump-day-good-morning-gif-13998484", #animated camel
    "https://cdn.discordapp.com/attachments/855980303570042910/874153351640653824/giphy-4.gif", #wacky wednesday bubbles guy
    "https://cdn.discordapp.com/attachments/855980303570042910/874153433320550420/200.gif", #fight club
    "https://cdn.discordapp.com/attachments/855980303570042910/874153521975541790/200-1.gif", #disco
    "https://cdn.discordapp.com/attachments/855980303570042910/874153595753365556/1afd7d9fe2922b353faf6d0b7fe7c50f.gif", #drunk lady in yard
  ],
  [ #THURSDAY
    "thursday",
    "https://tenor.com/view/thursday-happy-thursday-unicorn-dragging-rainbow-gif-15254014",
    "https://tenor.com/view/thursday-confetti-happy-thursday-celebrate-gif-11705413", #baby blue 70s suit guy
    "https://tenor.com/view/thursday-friday-funny-when-you-thought-its-fridayn-its-only-thursday-gif-15583680", #angrycat
    "https://tenor.com/view/thor-happy-thors-day-happy-thursday-chris-hemsworth-gif-17543834",
    "https://tenor.com/view/donald-duck-quacky-thursday-thursday-excited-gif-12381146",
    "https://cdn.discordapp.com/attachments/855980303570042910/874153923403989022/giphy-5.gif", #data high five
    "https://cdn.discordapp.com/attachments/855980303570042910/874154095592751144/200-3.gif", #frog dude pet a cat
    "https://cdn.discordapp.com/attachments/855980303570042910/874154160642216058/097c9abc18f3ceaad5040b7ad3600130.gif", #looking over wall
    "https://cdn.discordapp.com/attachments/855980303570042910/874154244633165915/giphy-6.gif", #chalkboard
    "https://cdn.discordapp.com/attachments/855980303570042910/874154309737119794/200w-1.gif", #burn after reading
    "https://c.tenor.com/DPVIwmxEmgYAAAAC/happy-thursday.gif", #thursday blessings
  ],
  [ #FRIDAY
    "FRIday",
    "https://tenor.com/view/nicolas-cage-friday-feel-that-friday-feeling-feel-that-thats-friday-gif-12235300",
    "https://tenor.com/view/time-to-do-friday-dance-cat-kittens-dancing-dance-moves-gif-16362746", #terribly photoshopped cat dance
    "https://tenor.com/view/ant-man-when-its-friday-excited-tgif-gif-11962947", #paul rudd
    "https://tenor.com/view/purrfect-its-friday-cat-kitten-kitty-gif-16398687", #cat in box with disco ball and deal with it glasses
    "https://tenor.com/view/its-friday-friday-dance-kermit-excited-happy-gif-12639745",
    "https://cdn.discordapp.com/attachments/855980303570042910/874154726994886707/giphy-7.gif", #surfing grandma
    "https://cdn.discordapp.com/attachments/855980303570042910/874154814475485204/Friday-23.gif", #joey tribbiani eating pizza
    "https://cdn.discordapp.com/attachments/855980303570042910/874154913570115615/giphy-8.gif", #office guy humping desk
    "https://c.tenor.com/ldnhJe8zeBUAAAAC/jumma-mubarak-good-morning.gif", #blessings
  ],
  [ #SATURDAY
    "SATURDAY",
    "https://tenor.com/view/yeah-baby-funny-oh-yeah-its-saturday-gif-15025789", #tina from bob's burgers
    "https://tenor.com/view/svaradiofm-happy-saturday-make-the-most-of-this-day-laugh-love-read-just-be-happy-gif-15042816",
    "https://tenor.com/view/hello-top-of-the-morning-top-hat-cat-cheerio-gif-13926359", #caturday with hat
    "https://tenor.com/view/saturday-dance-old-dancing-party-hard-gif-11712974", #grandma in the kitchen with friends
    "https://tenor.com/view/its-caturday-its-saturday-weekend-caturday-kittens-in-toilet-gif-21186885", #cats in 3d toilets
    "https://cdn.discordapp.com/attachments/855980303570042910/874155618863308820/giphy-downsized-large.gif", #chill dachshund
  ],
  [ #SUNDAY
    "sundayyyy",
    "https://tenor.com/view/lovely-sunday-have-a-good-day-flowers-butterfly-gif-8661074", #(((hugs)))
    "https://tenor.com/view/sunday-gif-10898789", #scribble (one of a series I didn't get)
    "https://tenor.com/view/peaceful-have-a-blessed-sunday-sunday-blessed-gif-14992878", #places in the world, vertical
    "https://tenor.com/view/sunday-good-morning-happy-gif-18599333", #special blend of blessings for you
    "https://tenor.com/view/butterfly-yellow-rose-sunday-hug-gif-12778265", #butterfly on flower
    "https://cdn.discordapp.com/attachments/855980303570042910/874155695329669120/200w-2.gif", #couch dachshund
    "https://c.tenor.com/jNlvxznV_6cAAAAd/happy-funday-sunday.gif", #reverse mimosa
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
      await message.channel.send(random.choice(genericResponses))
      # await message.channel.send(random.choice(whoResponses))
    elif "day" in message.content or "date" in message.content:
      await message.channel.send(random.choice(weekdays[today.weekday()]))
    else:
      await message.channel.send(random.choice(genericResponses))
    return

client.run(TOKEN)
