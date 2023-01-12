import random
import discord
from dotenv import load_dotenv
import os
import re
import twitter


load_dotenv()
TOKEN = os.getenv("TOKEN")
print(TOKEN)



intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True
client = discord.Client(intents=intents)


igregex = re.compile(r'https?://(www\.)?instagram\.com/(reel|p|stories)/\w+')
twregex = re.compile(r'https?://(www\.)?(mobile\.)?twitter\.com/\w+/status/\d+')

# read config/frases.txt into array
with open('config/frases.txt', 'r') as f:
    frases = f.readlines()

if len(frases) == 0:
    frases = ["Aqui está um link mais amigável para o Discord:"]

@client.event
async def on_ready():
    print(f'\n\n\n\n\n\n\nWe have logged in as {client.user}')

@client.event
async def on_message(message):
    new_url = None
    if igregex.match(message.content):
        url_match = re.search(r"https?://(www\.)?instagram\.com[/\w-]*", message.content)
        if url_match:
            url = url_match.group(0)
            new_url = url.replace("instagram.com", "ddinstagram.com")

    if twregex.match(message.content):
        if twitter.twt_is_video(message.content):
            url_match = re.search(r"https?://(www\.)?twitter\.com[/\w-]*", message.content)
            if url_match:
                url = url_match.group(0)
                if twitter.twt_is_video(url):
                    new_url = url.replace("twitter.com", "fxtwitter.com")

    if twregex.match(message.content):
        if twitter.twt_is_video(message.content):
            url_match = re.search(r"https?://mobile.twitter\.com[/\w-]*", message.content)
            if url_match:
                url = url_match.group(0)
                if twitter.twt_is_video(url):
                    new_url = url.replace("mobile.twitter.com", "fxtwitter.com")


    if new_url:
        frase = frases[random.randint(0, len(frases)-1)]
        await message.channel.send(frase + "\n" + new_url.split("?")[0])

    return 1




client.run(TOKEN)
