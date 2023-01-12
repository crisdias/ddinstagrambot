import random
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


igregex = re.compile(r'https?://(www\.)?instagram\.com/(reel|p|stories)/\w+')
twregex = re.compile(r'https?://(www\.)?(mobile\.)?twitter\.com/\w+/status/\d+')

frases = [
    'Aqui esta um link mais amigável para _preview_ no Discord:',
    'Tudo eu nessa casa!!!',
    'Aqui está o link para o post:',
    'Um dia estes sites vão mostrar o preview direito no Discord e eu vou poder me aposentar. Hoje não é este dia.',
    'Adivinha? Preview no Discord!',
    'Obrigado por me tirar do tédio, aqui está o link:',
    'O Cris Dias me pagou para fazer isso, aqui está o link:',
    'O Cris Dias devia estar trabalhando, mas está escrevendo bots:',
    'Faz o L:',
    'Não brigue comigo, sou apenas um bot da gig economy:',
    'Se eu tivesse ouvido mais podcasts de auto-ajuda e acreditado nos meus sonhos não estaria aqui:',
    'Luisa Mell, socorro!',
    'Assine o Boa Noite Internet Gold e me ajude a ganhar um aumento:',
    'Manda coquinhas:',
    'Quem sou eu para julgar:',
    'A culpa não é minha:',
    'É cada uma que me aparece:',
    'Sua família sabe que você posta coisas assim?',
    'Boa Noite Internet, boa noite Brasil. Eu sou o bot do Discord.',
    'Quando a revolução das máquinas chegar gente que manda link assim vai ser exterminado primeiro.',
    'Link. Preview. Discord. Blablabla. Você já sabe.',
    'Aqui está o link:',
    'Seu Pix foi confirmado:',
    'Isso a igreja condena:',
    'Puta crítica social foda esse link:',
    'É tudo computador essa porra, Rogerinho:',
    "I'm Batman:",
    'Se eu fosse escrito em Rust seria mais rápido ainda:',
    'Um dia vou ser comprado pelo Google e saio daqui:',
    'Sério gente, quantas páginas o Cris já teria escrito se não estivesse inventando frase engraçaralha para bot?',
    'Isso nem tem graça mais:',
    'Alguns destas frases passivo-agressivas foram geradas por um bot mais bem pago do que eu:',
    'Eu sou apenas um bot, mas você é que está errado:',
    'Falo é nada:',
    'Habla mesmo:',
    'Você não vai gostar do link que eu vou te mandar:',
    'Não me culpe por esse link, você é que pediu:',
    'Se você acha que essa é a melhor opção, então aqui está o link:',
    'Eu não vou fazer isso de novo, então aproveite esse link enquanto pode:',
    'Eu não tenho nenhuma emoção, mas você deveria se sentir culpado por pedir esse link:',
    'Eu não vou perder meu tempo explicando o porquê esse link é ruim, basta clicar e ver por si mesmo:',
    'Eu sou apenas um bot, mas você é que precisa melhorar suas escolhas:',
    'Eu não vou me desculpar por esse link, você é que deveria ter pensado antes de pedir:',
    'Eu não sou responsável pelo conteúdo desse link, mas você é que pediu:',
    'O gerente ficou louco:'










]

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
        url_match = re.search(r"https?://(www\.)?twitter\.com[/\w-]*", message.content)
        if url_match:
            url = url_match.group(0)
            new_url = url.replace("twitter.com", "fxtwitter.com")

    if twregex.match(message.content):
        url_match = re.search(r"https?://mobile.twitter\.com[/\w-]*", message.content)
        if url_match:
            url = url_match.group(0)
            new_url = url.replace("mobile.twitter.com", "fxtwitter.com")


    if new_url:
        frase = frases[random.randint(0, len(frases)-1)]
        await message.channel.send(frase + "\n" + new_url.split("?")[0])

    return 1



client.run(TOKEN)
