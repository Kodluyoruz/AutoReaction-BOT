import random
from discord.ext import commands

# Bot token'i token.0 dosyası içine yazıp oradan token değerine okutuyoruz
f = open("token.0", "r")
token = f.read()
f.close()

bot = commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
    print("Kodluyoruz BOT Aktif Hale Geldi!!")
    registerChannel = bot.get_channel(755411760386670693)
    await registerChannel.send("Merhabalar! Ben Kodluyoruz BOT! Kayd olabilir miyim lütfen?")
    
bot.run(token)