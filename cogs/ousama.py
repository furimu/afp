from discord.ext import commands
from utils import date
from discord import Embed
from random import shuffle, choice
import discord
import traceback
import asyncio


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_ousama = date.load('ousama')
        self.save_ousama = date.save
        self.join_member = []
    
    
    async def user_date(self, ctx, muter: str):
        self.load_ousama = date.load('ousama')
        guild = str(ctx.guild.id)

        for member in ctx.author.voice.channel.members:

            if muter == 'off':
                if member.bot:
                    continue
                else:
                    self.join_member.append(member.id)
            else:
                if member.voice.self_mute:
                    continue
                elif member.bot:
                    continue
                else:
                    self.join_member.append(member.id)


        voice = str(ctx.author.voice.channel.id)
        if self.load_ousama.get(guild, None) is None:
            self.load_ousama[guild] = {}
            self.save_ousama(self.load_ousama, 'ousama')

        if self.load_ousama[guild].get(voice, None) is None:
            self.load_ousama[guild][voice] = {}
            self.save_ousama(self.load_ousama, 'ousama')

        voice_key = self.load_ousama[guild][voice]
        vmembers = []
        self.load_ousama = date.load('ousama')
        while True:
            ousama = choice(self.join_member)
            
            if ctx.guild.get_member(ousama).bot:
                continue

            else:
                self.join_member.remove(ousama)
                break
        self.load_ousama[guild][voice]['ousama'] = str(ousama)
        self.save_ousama(self.load_ousama, 'ousama')
        
        for mem in self.join_member:

            if str(mem) != self.load_ousama[guild][voice]['ousama'] and not ctx.guild.get_member(mem).bot:
                vmembers.append(mem)

        shuffle(vmembers)

        counter = 1
        while True:
            for member in vmembers:
                self.load_ousama[guild][voice][str(counter)] = str(member)
                self.save_ousama(self.load_ousama, 'ousama')
                counter = counter + 1
            break


    @commands.command(name = '王様ゲーム')
    async def ousama(self, ctx, muter: str = 'on'):
        if not ctx.author.voice:
            return
        
        VCID = str(ctx.author.voice.channel.id)
        GUIDID = str(ctx.guild.id)
        
        await self.user_date(ctx, muter)
        
        embed = Embed(
            title = '王様ゲーム-Info | Version 1.0',
            description = ','.join(ctx.guild.get_member(memb).mention for memb in self.join_member),
            colour = ctx.author.color
        )
        
        embed.add_field(
            name = '王様',
            value = ctx.guild.get_member(int(self.load_ousama[GUIDID][VCID]['ousama'])).mention,
            inline = False
        )

        embed.add_field(
            name = f'**1番から{len(self.join_member)}**の中から番号で誰かを指定して命令してください',
            value = '命令が終わったら必ず**王様**が「n」と送信してください',
            inline = False
        )

        embed.set_footer(
            text = '王様ゲームを開始します'
        )

        await ctx.send(embed = embed)


        def start_check(mes):
            return mes.channel == ctx.channel and str(mes.author.id) == self.load_ousama[GUIDID][VCID]['ousama'] and mes.content == 'n'


        mes = await self.bot.wait_for('message', check = start_check)


        embed_ = Embed(
            title = '王様ゲーム-Info | Version 1.0',
            colour = ctx.author.color
        )
    
        for k, v in self.load_ousama[GUIDID][VCID].items():
            if not k == 'ousama':
                embed_.add_field(
                    name = k,
                    value = ctx.guild.get_member(int(v)).mention,
                    inline = False
                )

        embed_.set_footer(
            text = 'それでは王様ゲームをスタートします'
        )
        
        await ctx.send(embed = embed_)
        self.join_member.clear()

        self.load_ousama[GUIDID].pop(VCID)
        return self.save_ousama(self.load_ousama, 'ousama')

    @ousama.error
    async def ousama_error(self, ctx, error):
        dev = self.bot.get_user(386289367955537930)
        await ctx.send(f'{dev.mention}\n```py\n{traceback.format_exc()}\n```')

def setup(bot):
    bot.add_cog(Game(bot))