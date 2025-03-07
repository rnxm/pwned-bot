import discord
from discord.ext import commands
from discord import app_commands as apc
from dotenv import load_dotenv
import os
import asyncio
import platform
load_dotenv()

with open("leaked.txt", "r", encoding="utf8") as file:
    leaked_list = [line.strip().lower() for line in file.readlines()]

bot = commands.Bot(command_prefix="gvhndsfx;piuovfsdbiklhv", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} connected to Discord")
    await bot.tree.sync()

@bot.event
async def on_error(error: Exception):
    pass # ha nem megy hat nem megy

@bot.tree.command(description="Név vagy email alapján megnézi, hogy benne vagy-e a leakben.")
@apc.rename(email="e-mail", name="név")
@apc.describe(email="Az e-mail, amit számlázási e-mal címnek állítottál be előfizetésnél.",
              name="A név, amivel előfizettél. E-maillel egyszerűbb használni a parancsot.")
async def leaked(interaction: discord.Interaction, email: str = None, name: str = None):
    if not email and not name:
        return await interaction.response.send_message("Meg kell adnod vagy az e-mailed, vagy a nevedet!", ephemeral=True)

    if email and name:
        if email.lower() in [line.split(";")[1] for line in leaked_list] or name.lower() in [line.split(";")[0] for line in leaked_list]:
            return await interaction.response.send_message("# Az adataid (teljes név, e-mail cím, lakcím) benne vannak a kiszivárogtatott adatbázisban.\n**Mi a teendő?**\nAmennyiben úgy érzed, az adataidat jogtalanul kezelte a reFilc fejlesztője, jelentsd be az adatvédelmi incidenst a Nemzeti Adatvédelmi és Információszabadsági Hivatalnak ([NAIH](https://www.naih.hu/)).", ephemeral=True)

    if email:
        if email.lower() in [line.split(";")[1] for line in leaked_list]:
            return await interaction.response.send_message("# Az adataid (teljes név, e-mail cím, lakcím) benne vannak a kiszivárogtatott adatbázisban.\n**Mi a teendő?**\nAmennyiben úgy érzed, az adataidat jogtalanul kezelte a reFilc fejlesztője, jelentsd be az adatvédelmi incidenst a Nemzeti Adatvédelmi és Információszabadsági Hivatalnak ([NAIH](https://www.naih.hu/)).", ephemeral=True)
        else:
            return await interaction.response.send_message("# Az adataid nincsenek benne a kiszivárogtatott adatbázisban.", ephemeral=True)

    if name:
        if name.lower() in [line.split(";")[0] for line in leaked_list]:
            return await interaction.response.send_message("# Az adataid (teljes név, e-mail cím, lakcím) benne vannak a kiszivárogtatott adatbázisban.\n**Mi a teendő?**\nAmennyiben úgy érzed, az adataidat jogtalanul kezelte a reFilc fejlesztője, jelentsd be az adatvédelmi incidenst a Nemzeti Adatvédelmi és Információszabadsági Hivatalnak ([NAIH](https://www.naih.hu/)).", ephemeral=True)
        else:
            return await interaction.response.send_message("# Az adataid nincsenek benne a kiszivárogtatott adatbázisban. Név alapján megnézni nem olyan biztos, hogy helyesen találja meg az adatot, így ajánlatos emailt használni.", ephemeral=True)

@bot.tree.command(description="Adatvédelmi Tájékoztató")
async def privacy(interaction: discord.Interaction):
    await interaction.response.send_message("Az adatok, amiket parancsokként beírsz, a bot fejlesztői nem látják.\nA kiszivárgott adatok publikusan nincsenek megosztva a fejlesztők legjobb tudomása szerint, viszont ha az megtörténik, azért nem vállalunk felelősséget. A fájl, ahonnan beolvassuk és megnézzük, hogy a szivárgás tartalmazza-e a te adataidat, csak a több biztonsági réteggel is védett szerverünkön található meg.\nAz adataiddal a fejlesztők nem élnek vissza, és arról nem kapunk értesítést, ha mégis benne vannak az adataid.\n\nForráskód: https://github.com/rnxm/pwned-bot",
                                            ephemeral=False if interaction.guild else True)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
bot.run(os.getenv("TOKEN"))