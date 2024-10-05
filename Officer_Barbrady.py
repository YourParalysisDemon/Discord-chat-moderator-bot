import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# --Delete list--
block_words = ["add words here"]


@client.event
async def on_ready():
    print(f"Bot Logged in as {client.user}")


@client.event
async def on_message(msg):

    if msg.author != client.user:
        for text in block_words:    # roles that can post
            if "Trusted" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete()
                await msg.channel.send("Move along nothing to see here.", delete_after=1)
                return
            if any([hasattr(a, "width") for a in msg.attachments]):
                await msg.delete()
                await msg.channel.send("Move along nothing to see here.", delete_after=1)


# Bot token
client.run("token here")
