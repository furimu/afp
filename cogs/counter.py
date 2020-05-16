from discord.ext import commands
import discord
import random
class Count(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='ランダム')
    async def np(self, ctx, role:discord.Role):
        vcm= []
        for member in role.members:
            if member.voice is not None and member.voice.channel.id == ctx.author.voice.channel.id:
                vcm.append(member.id)

        random.shuffle(vcm)

        e = discord.Embed(
            description=',\n'.join(ctx.guild.get_member(m) for m in vcm)

        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Count(bot))