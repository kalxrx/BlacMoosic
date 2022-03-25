from discord.ext import commands

class contact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def contact(self, ctx):
        await ctx.send("Email- kalarunandasena@gmail.com \n Discord- kaluuux#8874")

def setup(bot):
    bot.add_cog(contact(bot))