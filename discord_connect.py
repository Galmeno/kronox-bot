#discord_connect.py
import discord
import secret_token
import kbot
from kbot import msg_dva248#, msg_dva340
client = discord.Client()

@client.event
async def on_ready():
    kbot.logger('#login')
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!schema DVA248'):
        kbot.logger('#1')
        for line in msg_dva248:
            await message.channel.send(line)
    #if message.content.startswith('!schema DVA340'):
    #    kbot.logger('#2')
    #    for line in msg_dva340:
    #        await message.channel.send(line)
    if message.content.startswith('!question help'):
        kbot.logger("#4 question help")
        await message.channel.send("Anonymous question posting (can be done with PM to bot):")
        await message.channel.send("*Post a question: !question DVA248 What does __init__ mean?")
        await message.channel.send("*Show questions: !show questions DVA248")
        await message.channel.send("*(WORK IN PROGRESS) Pop question: !pop DVA248 #1")

    elif message.content.startswith('!question '):
        kbot.logger("#4 new question")
        kbot.add_question(message.content[10:16],message.content[17:])
        await message.channel.send("Question logged")

    if message.content.startswith('!show questions '):
        kbot.logger("#5")
        questions = kbot.show_questions(message.content[16:22])
        i = 1
        for question in questions:
            await message.channel.send(f"{i}: {question}")
            i += 1
    
    if message.content.startswith('!del question '):
        kbot.logger("#6")
        questions = kbot.del_question(message.content[14:20],message.content[21:])
        await message.channel.send(f"{message.content[14:20]}: {message.content[21:]} deleted.")

    if message.content.startswith('!schema help'):
        kbot.logger('#3')
        await message.channel.send("Tillgängliga kurser:")
        await message.channel.send("DVA248")
        #await message.channel.send("DVA340")
        await message.channel.send("- - - - - - - - - - - - - - - - ")
        await message.channel.send("Visa schema med: !schema kurskod")
    
    #social
    if message.content.startswith('KXBot'):
        await message.channel.send('At your service!')  
    #end social

client.run(secret_token.token)