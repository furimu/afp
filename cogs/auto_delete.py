from discord.ext import commands, tasks
from discord import TextChannel, Embed, errors
from utils import date
from datetime import datetime

import traceback


class Auto_Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load = date.load('auto_delete')
                        
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ad_add(self, ctx, channels: commands.Greedy[TextChannel]):
        for channel in channels:

            if self.load.get('auto_delete', None) is None:
                self.load['auto_delete'] = []
                date.save(self.load, 'auto_delete')
            if str(channel.id) not in self.load['auto_delete']:
                self.load['auto_delete'].append(str(channel.id))
                date.save(self.load, 'auto_delete')
                await ctx.send(f'{channel.name}を登録しました！')
            else:
                await ctx.send('そのチャンネルは既に登録されています')

    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ad_re(self, ctx, channels: commands.Greedy[TextChannel]):

       
        for channel in channels:

            if self.load.get('auto_delete', None) is None:
                await ctx.send('そのチャンネルは登録されていません')
            if str(channel.id) in self.load['auto_delete']:
                self.load['auto_delete'].remove(str(channel.id))
                date.save(self.load, 'auto_delete')
                await ctx.send(f'{channel.name}の登録を解除しました')
            else:
                await ctx.send('そのチャンネルは登録されていません')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ad_(self, ctx, enable: str, channels: commands.Greedy[TextChannel] = None):
        
        if channels is None:
            channels = []
            channels.append(ctx.channel)
        for channel in channels:
            if enable == 'on':
                self.load[str(channel.id)] = enable
                date.save(self.load, 'auto_delete')
                await ctx.send(f'{channel.name}のAuto Deleteをオンにしました')

            elif enable == 'off':
                self.load[str(channel.id)] = enable
                date.save(self.load, 'auto_delete')
                await ctx.send(f'{channel.name}のAuto Deleteをオフにしました')
            else:
                await ctx.send('**afp:ad_ on or off**で入力してね(´・ω・`)')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ad_ree(self, ctx, channels: commands.Greedy[TextChannel] = None):
        
        if channels is None:
            channels = []
            channels.append(ctx.channel)
        for channel in channels:
            self.load.pop(str(channel.id))
            date.save(self.load, 'auto_delete')
            await ctx.send(f'{channel.name}のAuto Deleteの設定を解除しました')



    @commands.command()
    async def ad_list(self, ctx):
        

        a=[]
        

        for o in self.load['auto_delete']:
            try:
                print(self.bot.get_channel(int(o)).name)
                a.append(o)
            except:
                continue


        e = Embed(
            title = '登録してるチャンネル',
            description = ','.join(self.bot.get_channel(int(x)).mention for x in a)
        )
        for k, v in self.load.items():
            if k != 'auto_delete':
                try:
                    print(self.bot.get_channel(int(k)).name)
                    channel = self.bot.get_channel(int(k))
                except:
                    continue
                date.save(self.load, 'auto_delete')
                e.add_field(
                    name = channel.name,
                    value = self.load[str(channel.id)],
                    inline = False
                )

        await ctx.send(embed = e)


def setup(bot):
    bot.add_cog(Auto_Delete(bot))