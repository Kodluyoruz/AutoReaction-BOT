from discord.ext import commands

f = open("token.0", "r")
token = f.read()
f.close()

bot = commands.Bot(command_prefix="#")
emojis = [":whitemehaha:791189662055137281", ":kodluyoruz1:791195202748022784", ":kodluyoruz2:791195244662095872", ":kodluyoruz3:791195281734893579"]

@bot.event
async def on_ready():
    print("Kodluyoruz BOT has landed !")

@bot.event
async def on_message(message):
    if(message.channel.id == 791160980510867456):
        for i in emojis:
            await message.add_reaction(i)
    else:
        pass

bot.run(token)