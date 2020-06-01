from discord.ext import commands
import discord

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def p(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        boy = self.bot.get_channel(619930353267769344)
        girl = self.bot.get_channel(619930418573213719)

        async for message in boy.history(limit=None):
            if message.author == member:
                return await ctx.send(f"{str(message.author)}さんのプロフィールはこちらです。{message.jump_url}")

        else:
            async for message in girl.history(limit = None):
                if message.author == member:
                    return await ctx.send(f"{str(message.author)}さんのプロフィールはこちらです。{message.jump_url}")

def setup(bot):
    bot.add_cog(Send_Profile(bot))