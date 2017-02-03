import discord
import asyncio
from awbot.roll import roll
from awbot.char import char

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as [" + client.user.name + "]")


@client.event
async def on_message(message):
    split = message.content.split(' ')
    if split[0] == '!roll':
        await client.send_message(message.channel, message.author.mention + " rolled:\n" + roll(' '.join(split[1:])))
    elif split[0] == '!char':
        await char(message, split[1:])

