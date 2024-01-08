import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

# Inicializa el bot con los intents
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
category_name = 'sanciones'


load_dotenv()
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('------')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! {round(client.latency * 1000)}ms')

@client.command()
async def ban(ctx, username: str):
    
    # Revisa si el mensaje tiene archivos adjuntos
    if not ctx.message.attachments:
        await ctx.send("No hay archivos adjuntos en el mensaje.")
        return
    
    attachments = ctx.message.attachments
    #files = [{'file': (attachment.filename, await attachment.read(), attachment.content_type) for attachment in attachments}]
    files = []
    for index, attachment in enumerate(attachments):
        files.append((f'file{index}', (attachment.filename, await attachment.read(), attachment.content_type)))
    
    if files:
        auth_data = {'username': username}
        url = 'http://95.216.139.171/user/executeBan'
        headers = {'Host': "sa.playsoulcraft.net"}
        resp = requests.post(url, headers=headers, data=auth_data, files=files)
        print(resp)
    else:
        print("No se encontraron archivos.")

@client.command()
async def get(ctx, username: str):
    url = "https://sa.playsoulcraft.net/";
    return await ctx.send(url + username)   

@client.command()
async def home(ctx):
    await ctx.send("https://sa.playsoulcraft.net/")


client.run(token)