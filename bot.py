import discord, json
from discord.ext import commands

client = commands.Bot(description="Image Archiver by https://alf.wtf/", command_prefix="$", case_insensitive=True)

@client.event
async def on_ready():
    print(f'Logged in - https://alf.wtf/')
    await client.change_presence(activity=discord.Streaming(name="Image Archiver made by https://alf.wtf/", url="https://twitch.tv/ninja"))

@client.command()
async def archive(ctx, channel : discord.TextChannel):
    image_types = ["png", "jpeg", "gif", "jpg"]

    async for message in channel.history(limit=200):
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in image_types):
                await attachment.save(attachment.filename)

@client.command()
async def transfer(ctx, channel : int,  output : int):
    image_types = ["png", "jpeg", "gif", "jpg"]

    channel = client.get_channel(channel)
    output = client.get_channel(output)

    async for message in channel.history(limit=200):
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in image_types):
                url = str(attachment.url)
                await output.send(url)

with open('./config.json') as f:
    config = json.load(f)

token = config.get("token")
client.run(token, bot=True)
