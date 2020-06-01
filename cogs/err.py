from discord.ext import commands
import traceback
import discord
class Error(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("そのコマンドは存在しないよ！")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("あなたの権限が無いから実行出来ないよ")
 
        else:
            msg= list(traceback.TracebackException.from_exception(error).format())
            for i in range(0, len(msg), 1092):
                await ctx.channel.send(f'```py\n{msg[i:i+1092]}\n```')
 
 
    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        err=self.bot.get_channel(714735564641009785)
 
        msg= list(traceback.TracebackException.from_exception(error).format())
        for i in range(0, len(msg), 1092):
            await err.send(f'```py\n{msg[i:i+1092]}\n```')
 
def setup(bot):
    bot.add_cog(Error(bot))