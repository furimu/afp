from discord.ext import commands, tasks
from discord import TextChannel, Embed, errors
from utils import date
from datetime import datetime

import traceback


class Auto_Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load = date.load('auto_delete')
        self.audel.start()


    def cog_unload(self):
        self.audel.cancel()


    @tasks.loop(minutes = 1)
    async def audel(self):
        
        await self.bot.wait_until_ready()
        admin = self.bot.get_channel(679693385224945740)
        self.load = date.load('auto_delete')

        if not self.load.get('auto_delete'):
            return

        err_= []
        for channel in self.load['auto_delete']:
            if channel is None:
                continue
            if str(channel) in self.load.keys():
                
                target = self.bot.get_channel(int(channel))
                if target is None:
                    continue
                if self.load[str(target.id)] == 'on':
                    
                    async for message in target.history(limit = None):

                        if message.id == [687313132829540499, 650404155227242509, 650403128314953738]:
                            continue
                        try:
                            now = datetime.now()

                            if now.day == 1 and message.created_at.day == 25:
                                await message.delete()

                            elif now.day == 2 and message.created_at.day == 26:
                                await message.delete()
                            
                            elif now.day == 3 and message.created_at.day == 27:
                                await message.delete()

                            elif now.day == 4 and message.created_at.day == 28:
                                await message.delete()

                            elif now.day == 5 and message.created_at.day == 29:
                                await message.delete()

                            elif now.day == 6 and message.created_at.day == 30:
                                await message.delete()

                            elif now.day == 7 and message.created_at.day == 31:
                                await message.delete()

                            elif now.day == 1 and message.created_at.day == 24:
                                await message.delete()

                            elif now.day == 2 and message.created_at.day == 25:
                                await message.delete()

                            elif now.day == 3 and message.created_at.day == 26:
                                await message.delete()

                            elif now.day == 4 and message.created_at.day == 27:
                                await message.delete()

                            elif now.day == 5 and message.created_at.day == 28:
                                await message.delete()

                            elif now.day == 6 and message.created_at.day == 29:
                                await message.delete()

                            elif now.day == 7 and message.created_at.day == 30:
                                await message.delete()

                            elif now.day == 1 and message.created_at.day == 23:
                                await message.delete()

                            elif now.day == 2 and message.created_at.day == 24:
                                await message.delete()

                            elif now.day == 3 and message.created_at.day == 25:
                                await message.delete()

                            elif now.day == 4 and message.created_at.day == 26:
                                await message.delete()

                            elif now.day == 5 and message.created_at.day == 27:
                                await message.delete()

                            elif now.day == 6 and message.created_at.day == 28:
                                await message.delete()

                            elif now.day == 7 and message.created_at.day == 29:
                                await message.delete()

                            elif now.day == 1 and message.created_at.day == 22:
                                await message.delete()

                            elif now.day == 2 and message.created_at.day == 23:
                                await message.delete()

                            elif now.day == 3 and message.created_at.day == 24:
                                await message.delete()

                            elif now.day == 4 and message.created_at.day == 25:
                                await message.delete()

                            elif now.day == 5 and message.created_at.day == 26:
                                await message.delete()

                            elif now.day == 6 and message.created_at.day == 27:
                                await message.delete()

                            elif now.day == 7 and message.created_at.day == 28:
                                await message.delete()
                            
                            elif datetime.now().day - message.created_at.day  >= 7:
                                await message.delete()

                            continue



                        except errors.Forbidden:
                            err_.append(target.id)

                        except:
                            await admin.send(f'```py\n{traceback.format_exc()}\n```')
        e=Embed(title="以下のチャンネルでメッセージを削除する権限がありません", description=f"{self.bot.get_channel(e).mention for e in err_}")
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Auto_Delete(bot))