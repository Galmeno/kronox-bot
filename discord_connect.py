#discord_connect.py
import discord
import secret_token
from kbot import msg_dva128, msg_dva131, resurser
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!schema DVA128'):
        for line in msg_dva128:
            await message.channel.send(line)
    #if message.content.startswith('$schema dva131'):
    #    for line in msg_dva131:
    #        await message.channel.send(line)
    if message.content.startswith('!schema help'):
        await message.channel.send("Tillgängliga kurser:")
        await message.channel.send("DVA128")
        #await message.channel.send("DVA131")
        await message.channel.send("- - - - - - - - - - - - - - - - ")
        await message.channel.send("Visa schema med: !schema kurskod")

client.run(secret_token.token)