import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)



@bot.event
async def on_ready():
    print("I am ready")


@bot.command()
async def musor(ctx):
    await ctx.send("""
                   Пластик разлагается от 400 до 700 лет
                   Металл в чистом виде они редко встречаются, в основном в виде сплавов, но и если брать их в условном «чистом» состоянии, то они обладают различными свойствами и скорость их разложения будет сильно отличаться 
                   Стекло очень долго разлагается, около 1000 лет
                   Резина разлагается от 120-140 лет
                   Бумажки разлагаются 1-2 месяца
                   Брошенные стоящие машины разлагаются от 10 до 20 лет
                   """)
    










bot.run()
