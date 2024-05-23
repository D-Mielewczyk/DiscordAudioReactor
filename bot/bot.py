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
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)


@bot.tree.command(name="join", description="Make the bot join your current voice channel")
async def join(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        await channel.connect()
        await interaction.response.send_message(f"Joined voice channel: {channel.name}")
        logger.info('Joined voice channel: %s', channel.name)
    else:
        await interaction.response.send_message("You are not connected to a voice channel")
        logger.info('User %s is not connected to a voice channel', interaction.user)


@bot.tree.command(name="leave", description="Make the bot leave the voice channel")
async def leave(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client
    if voice_client:
        channel_name = voice_client.channel.name
        await voice_client.disconnect()
        await interaction.response.send_message("Left the voice channel")
        logger.info('Left voice channel: %s', channel_name)
    else:
        await interaction.response.send_message("Bot is not connected to a voice channel")
        logger.warning('Attempted to leave voice channel but bot is not connected')


bot.run(TOKEN)
