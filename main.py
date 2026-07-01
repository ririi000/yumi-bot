import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# THIS IS THE COG LOADER (you replace old stuff with this)
async def load_cogs():
    await bot.load_extension("cogs.economy")
    await bot.load_extension("cogs.inventory")
    await bot.load_extension("cogs.shop")

@bot.event
async def setup_hook():
    await load_cogs()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
