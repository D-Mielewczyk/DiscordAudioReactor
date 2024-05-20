import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # Ensure you have the right intents

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not connected to a voice channel")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    keywords = {
        "hello": "path/to/hello.mp3",
        "bye": "path/to/bye.mp3"
    }
    
    for keyword, filepath in keywords.items():
        if keyword in message.content.lower():
            if message.guild.voice_client is not None:
                source = discord.FFmpegPCMAudio(filepath)
                message.guild.voice_client.play(source)
            else:
                await message.channel.send("Bot is not connected to a voice channel")
            break
    
    await bot.process_commands(message)

bot.run(TOKEN)
