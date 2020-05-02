from discord.ext import commands, tasks
from discord import VoiceChannel, Role
from utils.date import *
from cogs.game_plugin import enit, start, set_cha, create_number, webhooks, loop_time
import traceback
class Ousama(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player_ = load('ousama_')


    @tasks.loop(minutes = 1)
    async def ousama_notice(self):
        afp = self.bot.get_guild(619926767821652000)
        for vc in afp.voice.channels:
            if not self.player_.get(str(vc.id)):
                continue

            else:
                if loop_time.hour_check(vc) == False:
                    continue
                elif loop_time.mintue_check(vc) == False:
                    continue
                else:
                    for text_ in voice_channel.category.text_channels:
                        await text_.edit(name = '王様ゲーム')

                    channel = self.bot.get_channel(int(self.player_[str(vc.id)]['text']))
                    return await channel.send('時間五分前です。')

        
    #王様ゲームのメインコマンド
    #聞き専有り
    @commands.group(name = '王様ゲーム+', invoke_without_command = True)
    async def ousama_(self, ctx, muter = 'on'):
    
        vc = str(ctx.author.voice.channel.id)
        
        if muter != 'off':
            if await enit.check_mute(ctx) == True:
                return

        if await enit.check_join_voice_channel(ctx) == True:
            return

        set_cha.set_main(ctx)
        ousama_master = ctx.guild.get_member(int(self.player_[vc]['ousama_']))
        await ctx.send('王様ゲーム Info\n 参加してるメンバー一覧' + 'さん,'.join(ctx.guild.get_member(member).mention for member in self.player_[vc]['list_']))
        await ctx.send(f'王様{ousama_master.mention}')
        await ctx.send(f"**1番から{len(self.player_[vc]['list_'])}**の中から番号で指定してください\n 命令が終わったら必ず、**{ousama_master.mention}**さんが [n]と送信してください")
        def start_check(mes):
            return mes.channel == ctx.channel and str(message.author.id) == ousama_master and mes.content == 'n'

        mes = await self.bot.wait_for('message', check = start_check)

        await ctx.channel.edit(topic = mes.content)

        e = create_number.send_number(ctx)
        await ctx.send(embed = e)

        for k in self.player_[vc].keys():
            if k == 'list' or 'ousama_' or 'minute' or 'hour' or 'Recruitment':
                continue
            
            self.player_[vc].pop(k)
            return save(self.player_, 'ousama_')


    @ousama_.command(name = '開始')
    async def ousma_start(self, ctx, voice_channel: VoiceChannel, mention: commands.Greedy[Role], start_time: str):
        VCID = str(voice_channel.id)

        hour, minute = start.time_split(start_time)

        if self.player_.get(VCID):
            return

        save_key('ousama_', VCID, [], 'list_')

        for time in [hour, minute]:
            await start.check_times(ctx, time)

        await start.check_time(VCID, hour, minute)
        start.set_message_id(ctx, VCID)
        start.set_game_master(ctx, VCID)
        for text in voice_channel.category.text_channels:
            self.player_[VCID]  = dict()
            self.player_[VCID]['text'] = str(text.id)
            self.player_[VCID]['before_text_name'] = text.name
            self.player_[VCID]['before_vocie_name'] = voice_channel.name
        
            save(self.player_, 'ousama_')

       
        mes = await webhooks.send_webhook(ctx=ctx, voice_channel = voice_channel, hour =hour, minute = minute, mention = mention)
        save_key('ousama_', VCID, str(mes.id), 'Recruitment')
        target_channel = self.bot.get_channel(ctx.channel.id)
        new_mes = await target_channel.fetch_message(mes.id)
        await new_mes.add_reaction('\U00002640')
        await new_mes.add_reaction('\U00002642')


    @ousma_start.error
    async def ousama_start_error(self, ctx, error):
        await ctx.send(f'```py\n{traceback.format_exc()}\n```')


    


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        
        for vc in payload.member.guild.voice_channels:
            if not self.player_.get(str(vc.id)):
                continue
            if self.player_[str(vc.id)].get("Recruitment"):
                if str(ctx.author.id) not in self.player_[str(vc.id)]['list_']:
                    self.player_[str(vc.id)]['list_'].append(str(ctx.author.id))
                    save(self.player_, 'ousama_')
                    return await ctx.send('ゲームへの登録が完了しました。')

                else:
                    return await ctx.send('貴方はすでにゲームに参加しています')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.member.bot:
            return
        
        for vc in payload.member.guild.voice_channels:
            if not self.player_.get(str(vc.id)):
                continue
            if self.player_[str(vc.id)].get("Recruitment"):
                if str(ctx.author.id) not in self.player_[str(vc.id)]['list_']:
                    self.player_[str(vc.id)]['list_'].remove(str(ctx.author.id))
                    save(self.player_, 'ousama_')
                    return await ctx.send('ゲームへの登録が完了しました。')
                    
                else:
                    return await ctx.send('貴方はすでにゲームに参加しています')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not self.player_.get(str(before.channel.id)):
            return

        elif len(after.channel.members) == 0:
            channel = self.bot.get_channel(int(self.player_[str(vc.id)]['text']))
            await channel.send('ボイスチャンネルから誰も居なくなったため、ゲームが終わったと判断しました\n お疲れさまでした')
            mes = await channel.send('今回のゲームで保存したデータを削除しています。。。')
            async with channel.typing():
                self.player_.pop(str(before.channel.id))
                save(self.player_, 'ousama_')
                await mes.edit('削除されました。')


def setup(bot):
    bot.add_cog(Ousama(bot))