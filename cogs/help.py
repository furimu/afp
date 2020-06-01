from discord.ext import commands
from discord import Embed
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):
        embed = Embed(
            title = f"{self.bot.user.name}のヘルプです",
            url = 'https://github.com/furimu/afp/blob/master/Readme.md')
        await ctx.send(embed= embed)


def setup(bot):
    bot.add_cog(Help(bot))