# filepath: /discord-vk-music-bot/discord-vk-music-bot/src/main.py
DISCORDTOKEN=


import discord
from discord.ext import commands
from discord_client import DiscordClient

# Инициализация бота
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Настройка событий
@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user}')

# Запуск бота
if __name__ == '__main__':
    bot_client = DiscordClient(bot)
    bot_client.run('DISCORDTOKEN')
