from discord.ext import commands
import discord
import random
import traceback
class Count(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("そのコマンドは存在しないよ！")
 
        else:
            msg= list(traceback.TracebackException.from_exception(error).format())
            for i in range(0, len(msg), 1092):
                await ctx.channel.send(f'```py\n{msg[i:i+1092]}\n```')

    @commands.command(name='ランダム')
    async def np(self, ctx, role:discord.Role):
        vcm= []
        for member in role.members:
            if member.voice is not None and member.voice.channel.id == ctx.author.voice.channel.id:
                vcm.append(member.id)

        random.shuffle(vcm)

        e = discord.Embed(
            description=',\n'.join(ctx.guild.get_member(m) for m in vcm))

        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Count(bot))