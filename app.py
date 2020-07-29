# bot.py
import os
from time import gmtime, strftime
import time
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

t = time.strftime("%I:%M:%S %p", time.gmtime())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!Time':
        
        await message.channel.send(t)

client.run(TOKEN)

#Made by Vulpes