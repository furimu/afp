from discord import Message
from discord.ext import commands
import traceback
author = Message.author
class Tester(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def tester(self, ctx):
        await ctx.send (f'=={author}')

    @tester.error
    async def tester_error(self, ctx, error):
        await ctx.send(f'```py\n{traceback.format_exc()}\n```')

def setup(bot):
    bot.add_cog(Tester(bot))