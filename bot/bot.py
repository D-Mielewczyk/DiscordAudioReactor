import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

PERMISSIONS_INTEGER = 630019156082624

# Configure logging
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("discord")

intents = discord.Intents.default()
intents.message_content = True  # Ensure you have the right intents

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    logger.info('Logged in as %s', bot.user)
    print(f'Invite your bot using the following URL: '
          f'https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions={PERMISSIONS_INTEGER}&scope=bot')



@bot.command()
@bot.tree.command(name="join", description="Make the bot join your current voice channel")
async def join(ctx: discord.Interaction):
    if ctx.user.voice:
        channel = ctx.user.voice.channel
        await channel.connect()
        await ctx.response.send_message(f"Joined voice channel: {channel.name}")
        logger.info('Joined voice channel: %s', channel.name)
    else:
        await ctx.response.send_message("You are not connected to a voice channel")
        logger.info('User %s is not connected to a voice channel', ctx.user)

@bot.tree.command(name="leave", description="Make the bot leave the voice channel")
async def leave(ctx: discord.Interaction):
    if ctx.guild.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.response.send_message("Left the voice channel")
        logger.info('Left voice channel: %s', ctx.guild.voice_client.channel.name)
    else:
        await ctx.response.send_message("Bot is not connected to a voice channel")
        logger.warning('Attempted to leave voice channel but bot is not connected')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    logger.info("Message from %s: %s", message.author, message.content)

    keywords = {"hello": "path/to/hello.mp3", "bye": "path/to/bye.mp3"}

    for keyword, filepath in keywords.items():
        if keyword in message.content.lower():
            if message.guild.voice_client is not None:
                source = discord.FFmpegPCMAudio(filepath)
                message.guild.voice_client.play(source)
                logger.info("Playing audio for keyword: %s", keyword)
            else:
                await message.channel.send("Bot is not connected to a voice channel")
                logger.warning(
                    "Attempted to play audio but bot is not connected to a voice channel"
                )
            break

    await bot.process_commands(message)


bot.run(TOKEN)
