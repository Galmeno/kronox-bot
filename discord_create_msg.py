#discord_create_msg.py
#https://discordpy.readthedocs.io/en/latest/index.html
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')