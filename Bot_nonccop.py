import discord
from discord.ext import commands
import random
import matplotlib.pyplot as plt
import numpy as np
import time as ti
spam_key = 1

#NON BUTTONS
TOKEN = '***' #здесь в ориганале должен быть прописан ID вашего бота(Заменён из соображений безопасности) 
PREFIX = 'mt_'
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = PREFIX, intents = intents)

@bot.command()
async def hi(ctx):
    await ctx.reply('Hello!') #ответ на сообщение-запрос
@bot.command()
async def say(ctx, data):
    await ctx.send(data)#отправка сообщения (печатает как юзер)
@bot.command()
async def rannums(ctx, p1, p2):
    await ctx.send('Your number:')
    await ctx.send(random.randint(int(p1), int(p2)))

@bot.command()
async def xiny(ctx, x, y):
    await ctx.send(f'{x}^{y} = {int(x)**(int(y))}')
@bot.command()
async def conv(ctx, ten):
    await ctx.send(bin(int(ten)))   
#BUTTONS
class MyView(discord.ui.View):
    @discord.ui.button(label='Click here', style = discord.ButtonStyle.blurple)
    async def button_callback(self, interaction, button):
        await interaction.response.send_message('|Bot Prefix - mt_|\n\n1 - hi(Hello world1!)\n2 - say(Your word)\n3 - rannums([From]:[To])\n4 - xiny([x]**[y])\n5 - conv([Your num]\n')
@bot.command()
async def commands(ctx):
    await ctx.send('Click for the list of commands!', view = MyView())


bot.run(TOKEN)
