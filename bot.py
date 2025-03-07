import discord
from discord.ext import commands
from discord import app_commands as apc
from dotenv import load_dotenv
import os
load_dotenv()

with open("leaked.txt", "r", encoding="utf8") as file:
    leaked = [line.strip() for line in file.split("\n")]

bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} connected to Discord")
    await bot.tree.sync()

@bot.tree.command(description="Név vagy email alapján megnézi, hogy benne vagy-e a leakben.")
async def leaked(interaction: discord.Interaction, email: str = None, name: str = None):
    if not email and not name:
        return await interaction.response.send_message("Meg kell adnod vagy az e-mailed, vagy a nevedet!", ephemeral=True)
    if email:
        if email in [line.split(";")[0] for line in leaked]:
            return await interaction.response.send_message("# Az adataid benne vannak a kiszivárogtatott adatbázisban.\n**Mi a teendő?**\nAmennyiben úgy érzed, az adataidat jogtalanul kezelte a reFilc fejlesztője, jelentsd be az adatvédelmi incidenst a Nemzeti Adatvédelmi és Információszabadsági Hivatalnak ([NAIH](https://www.naih.hu/)).", ephemeral=True)
        else:
            return await interaction.response.send_message("# Az adataid nincsenek benne a kiszivárogtatott adatbázisban.", ephemeral=True)
    if name:
        if email in [line.split(";")[1] for line in leaked]:
            return await interaction.response.send_message("# Az adataid benne vannak a kiszivárogtatott adatbázisban.\n**Mi a teendő?**\nAmennyiben úgy érzed, az adataidat jogtalanul kezelte a reFilc fejlesztője, jelentsd be az adatvédelmi incidenst a Nemzeti Adatvédelmi és Információszabadsági Hivatalnak ([NAIH](https://www.naih.hu/)).", ephemeral=True)
        else:
            return await interaction.response.send_message("# Az adataid nincsenek benne a kiszivárogtatott adatbázisban. Név alapján megnézni nem olyan biztos, hogy helyesen találja meg az adatot, így ajánlatos emailt használni.", ephemeral=True)

bot.run(os.getenv("TOKEN"))