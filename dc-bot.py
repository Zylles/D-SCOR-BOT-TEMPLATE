import discord
from discord.ext import commands
import kur
import utils
from game import *

intents = discord.Intents.all()


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix='/', intents=intents, *args, **kwargs)


bot = MyBot()


@bot.event
async def on_ready():
    print('!!!!-HAZIRIM-!!!!')


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelen-giden")
    await channel.send(f"{member} ARAMIZA KATILDI :) \n HOŞGELDİN")
    print(f"{member} ARAMIZA KATILDI :) \n HOŞGELDİN")


async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelen-giden")
    await channel.send(f"{member} ARAMIZDAN AYRILDI ): \n GÜLEGÜLE")
    print(f"{member} ARAMIZDAN AYRILDI ): \n GÜLEGÜLE")


@bot.command(name='Dolar')
async def hello(ctx):
    await ctx.send('DOLAR ŞU ANDA: ' + kur.dolar)


bot.command(name='Euro')


async def hello(ctx):
    await ctx.send('Euro ŞU ANDA: ' + kur.euro)


@bot.command(name='Bilgi')
async def hello(ctx):
    await ctx.send("CANLI EUROYU GÖRMEK İÇİN /Euro \n CANLI DOLARI  GÖRMEK İÇİN /Dolar")


# ------------------------------------TOKEN--------------------------------------
bot.run("MTIwNzAxNzI4NTE4MTUxMzc4OQ.G9DTtM.iQOzAFu6e1J0eSZvLkeSpVO4TKEh5jm0jp2Ob0")
