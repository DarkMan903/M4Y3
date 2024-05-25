import discord
import os
import random
from discord.ext import commands
from bot_cod import *


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def stop(self, ctx):
    """Stops and disconnects the bot from voice"""

    await ctx.voice_client.disconnect()

@bot.command()
async def join(self, ctx, *, channel: discord.VoiceChannel):
    """Joins a voice channel"""
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await channel.connect()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}! Вот список моих команд: ' + '\n')
    await ctx.send(f'1. stop_bot - команда досрочного отключения меня U+1F622' + '\n')
    await ctx.send(f'2. stop - выйти из голосового канала' + '\n')
    await ctx.send(f'2. join - совершить вход в голосовой канал;' + '\n')
    await ctx.send(f'3. heh с указанием цифры или числа - я начинаю смеяться, но у меня есть секрет :)'+ '\n')
    await ctx.send(f'4. mem - кидаю рандомный мем' + '\n')
    await ctx.send(f'5. mem_rarity - кидаю мем по редкости' + '\n')
    await ctx.send(f'6. rec - выдаю рандомную рекомендацию' + '\n')
    await ctx.send(f'Команда начинается со символа "$"')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    if count_heh == 6:
        await ctx.send(f'Trolling :)))')

@bot.command()
async def stop_bot(ctx):
    await ctx.send("Остановка бота...")
    await bot.close()
    
@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def mem_rarity(ctx):
    i = random.randint(1, 100)
    if i >= 91:
        await ctx.send(f"Выпало число(цифра): {i}. Редкий!!! Поздравляю!!!")
    else:
        await ctx.send(f"Выпало число(цифра): {i}")
    if i in range(1,50):
        with open('images/mem1.jpg', 'rb') as f:
            pictures = discord.File(f)
        await ctx.send(file=pictures)
    elif i in range(51, 90):
        with open('images/mem2.jpg', 'rb') as f:
            pictures = discord.File(f)
        await ctx.send(file=pictures)
    elif i in range(91, 100):
        with open('images/mem3.jpg', 'rb') as f:
            pictures = discord.File(f)
        await ctx.send(file=pictures)

@bot.command()
async def rec(ctx):
    recomm = ['Сортируйте мусор и выбрасывайте его по отдельности','Занимайтесь облагораживанием своего города','Экономьте топливо','Снижайте потребление электроэнергии','Экономьте воду']
    i = (random.choice(recomm))
    await ctx.send(f'Совет:{i}!')



bot.run("")
