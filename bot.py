import discord
from discord.ext import commands
# for loading the .env file
from dotenv import load_dotenv
# for file handling
import os
# for colored text
from colorama import Fore, Style

# load the discord token from the .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# create an instance of the bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


# load the cogs (commands) from the cogs folder
async def load_cogs():
    # iterate through the files in the cogs folder
    for filename in os.listdir("./cogs"):
        # check if the file is a python file and not the __init__.py file
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                # load the cog and slice the .py extension
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(Fore.GREEN + f"Successfully loaded cogs: {Fore.GREEN}{filename}")
                # error handling
            except Exception as e:
                print(f"Error loading {Fore.GREEN}{filename}: {Fore.RED}{e}")

@bot.event
async def on_ready():
    await load_cogs() # load the cogs in the on_ready function
    guild = discord.utils.get(bot.guilds, name="Your Server Name")
    await bot.tree.sync(guild=guild)
    print(Fore.BLUE + f"Hello, Arkitekx! All parameters have passed and the bot will now start.\n{Fore.GREEN}{bot.user}")
    print(Fore.YELLOW + "Bot is connected and ready!")

# run the bot
bot.run(DISCORD_TOKEN)
