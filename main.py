import random
from discord.ext import commands

# Bot token'i token.0 dosyası içine yazıp oradan token değerine okutuyoruz
f = open("token.0", "r")
token = f.read()
f.close()

bot = commands.Bot(command_prefix="#")

# Tüm emojilerin ID'leri ve isimleri aşağıda belirtilen listedeki şekilde listeye kayd edilmesi yeterlidir
emojis = [":onay:756165714020270211",
          ":kodluyoruzlogo:778245370534297610",
          ":kodluyoruzpurple:778245370694074368",
          ":kodluyoruzlightblue:778245370525515786",
          ":kodluyoruzyellow:778245370907721759",
          ":kodluyoruzaqua:778245370408861716",
          ":kodluyoruzblue:778245370073448459",
          ":kodluyoruzpink:778245370621853706",
          ":kodluyoruzblack:778245370332708904",
          ":kodluyoruzred:778245371066843147",
          "a:ucanroket:778244458377510912"]

@bot.event
async def on_ready():
    print("Kodluyoruz BOT Aktif Hale Geldi!!")

@bot.event
async def on_message(message):
    if(message.channel.id == 727896197624234034 or message.channel.id == 727896370845057055 or message.channel.id == 763038211890216980):
        random.shuffle(emojis)
        for i in emojis:
            await message.add_reaction(i)
    else:
        pass

bot.run(token)