import discord
from discord.ext import commands
from token import token_bot

cliente = commands.Bot(command_prefix=".")


@cliente.event
async def on_ready():
    print("Tamo ready mi pana")


@cliente.command(aliases=['alo?'])
async def alo(ctx):
    await ctx.send('toy volao?')


@cliente.command()
async def Ping(ctx):
    await ctx.send(f'Ping: {round(cliente.latency * 1000)}ms')


cliente.run(token)
