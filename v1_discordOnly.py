"""v1_discordOnly.py: The Discord Bot section of the project"""

__author__      = "Mac Lawson"
__copyright__   = "Copyright 2023"

import discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pull'):
        #call both methods
        #Customize this!
        await message.channel.send()        
        await message.channel.send()


client.run("")
