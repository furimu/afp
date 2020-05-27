from discord.ext import commands
from utils import date
import traceback
import asyncio
from datetime import datetime
COGS = [
    'admin',
    'auto_delete',
    'err',
    'loop_auto_delete',
    'ousama',
    'translation',
    'music',
    'quote'
]
prefix = date.load('prefix')

def prefix_call(bot, mes):
        default_prefix = 'afp:'
        id = str(mes.guild.id)
        if prefix.get(id, None) is None:
            prefix[id] = {}
        return prefix[id].get('prefix_list', default_prefix)

class Launc(commands.Bot):
    def __init__(self, cmd_prefix, description = None):
        super().__init__(cmd_prefix, description=description)

        self.token =  date.load('botinfo').get('token', '')       
        
        

        for cog in COGS:
            try:
                self.load_extension(f'cogs.{cog}')
            except Exception:
                print(traceback.format_exc())



    async def on_ready(self):
        print(f'{self.user.name}-LOGIN-{datetime.now()}')


    async def on_message(self, mes):
        if mes.author.bot:
            return

        await self.process_commands(mes)

    
    async def start(self):
        await super().start(self.token)

    def main(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())
        loop.close()


if __name__ == '__main__':
    _prefix = prefix_call
    desc = date.load('botinfo').get('desc', '')
    bot = Launc(_prefix, desc)
    bot.main()