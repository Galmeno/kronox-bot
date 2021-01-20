@client.event
async def on_message(msg):
    with open("answers.json", 'r') as f:
        inte = json.load(f)
    if not msg.author.id == client.user.id:
        if not msg.guild:
            intents = inte['intents']
            for intent in intents:
                tag = intent['tag']
                for patternz in intent['tag']:
                    #print(intent['tag']['patterns'])
                    if msg.content.lower() in tag['patterns']:
                        await msg.author.send(f"{tag['name']}, {random.choice(tag['responses'])}")
                        return
            await msg.author.send("Idek")
