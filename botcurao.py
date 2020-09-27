import discord
from discord.ext import commands
from tokendelbot import TOKEN_BOT


cliente = commands.Bot(command_prefix=".")

class carta():
    def __init__(self, numero, color):
        self.numero = numero
        self.color = color

colors = ["corazon", "diamante", "pica", "trebol"]
mazo = [carta(numero, color) for numero in range(1, 14) for color in colors]

@cliente.event
async def on_ready():
    print("Bot listo")


@cliente.command(aliases=['alo?'])
async def alo(ctx):
    await ctx.send('toy volao?')


@cliente.command()
async def Ping(ctx):
    await ctx.send(f'Ping: {round(cliente.latency * 1000)}ms')

@cliente.command()
async def caracol(ctx):
    embed = discord.Embed(
        title = "Caracol",
        decription = "Elige si la siguiente carta sera máyor o menor.",
        colour = discord.Color.blurple()
    )
    embed.set_footer("Elige si la siguiente carta sera máyor o menor.")
    await ctx.send(embed=embed)
    await embed_msg.add_reaction("👍")
    await embed_msg.add_reaction("👎")
    


cliente.run(TOKEN_BOT)
