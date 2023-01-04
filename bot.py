import discord
from dotenv import load_dotenv
import os
import re


load_dotenv()
TOKEN = os.getenv("TOKEN")
print(TOKEN)



intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if "https://www.instagram.com" in message.content:
        url_match = re.search(r"https?://(www\.)?instagram\.com[/\w-]*", message.content)
        if url_match:
            url = url_match.group(0)
            new_url = url.replace("instagram.com", "ddinstagram.com")
        await message.channel.send("Aqui esta um link mais amigavel para o Discord:\n" + new_url)

async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)
