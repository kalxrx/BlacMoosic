from discord.ext import commands
from webserver import keep_alive
import contact
import os

cogs = [contact]

bot = commands.Bot(command_prefix='*')

for i in range(len(cogs)):
    cogs[i].setup(bot)

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore'
    }
]

@bot.event
async def on_ready():
    print('Bot is ready to play Music')
    bot.load_extension('dismusic')

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run("TOKEN")