from discord.ext import commands
import discord
import random
import traceback
class Count(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

   

    @commands.command(name='ランダム')
    async def np(self, ctx, role:discord.Role):
        vcd = {}
        vcm= []
        for member in role.members:
            if member.voice is not None and member.voice.channel.id == ctx.author.voice.channel.id:
                vcm.append(member.id)

        random.shuffle(vcm)
        cou= 1
        for m in vcm:
            vcd[str(cou)]= m
            cou += 1

        e = discord.Embed(
            description=',\n'.join(f"{k}: {ctx.guild.get_member(m).mention}" for k, m in vcd.items()))

        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Count(bot))