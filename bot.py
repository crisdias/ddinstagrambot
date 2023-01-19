import random
import discord
from dotenv import load_dotenv
import os
import re
import twitter


load_dotenv()
TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
print(TOKEN)



intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True
client = discord.Client(intents=intents)


igregex = re.compile(r'https?://(www\.)?instagram\.com/(reel|p|stories)/[\w-]+')
twregex = re.compile(r'https?://(www\.)?(mobile\.)?twitter\.com/\w+/status/\d+')

# read config/frases.txt into array
with open('config/frases.txt', 'r') as f:
    frases = f.readlines()

if len(frases) == 0:
    frases = ["Aqui está um link mais amigável para o Discord:"]

@client.event
async def on_ready():
    print(f'\n\n\n\n\n\n\nWe have logged in as {client.user}')
    print(f'https://discordapp.com/api/oauth2/authorize?client_id={CLIENT_ID}&permissions=10304&scope=bot')

@client.event
async def on_message(message):
    # exit if message is from bot
    if message.author == client.user:
        return 1
        
    new_url = None
    igmatch = re.search(igregex, message.content)
    twmatch = re.search(twregex, message.content)

    if igmatch:
        url = igmatch.group(0)
        new_url = url.replace("instagram.com", "ddinstagram.com")

    if twmatch:
        url = twmatch.group(0)
        # if twitter.twt_is_video(url):
        new_url = url.replace("https://mobile.twitter.com/", "https://twitter.com/")
        new_url = url.replace("https://twitter.com", "https://fxtwitter.com")


    if new_url:
        frase = frases[random.randint(0, len(frases)-1)]
        await message.channel.send(frase + "\n" + new_url.split("?")[0])
        await message.edit(suppress=True)

    return 1




client.run(TOKEN)
