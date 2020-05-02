from discord.ext.commands import *
from discord import Embed

from utils.date import *

load_ousama = load('ousama_')

def time_split(start_time: str):
    hour = start_time.split(':')[0]
    minute = start_time.split(':')[1]
    return hour, minute


async def check_times(ctx, time_):
    if not time_:
        return await ctx.send('時間が指定されてません。')

async def check_time(vc, hour: str, minute: str):

    save_key('ousama_', vc, minute, 'minute')

    save_key('ousama_', vc, hour, 'hour')



def set_message_id(ctx, vc):
    save_key('ousama_', vc, str(ctx.message.id), 'message_id')

def set_game_master(ctx, vc):
    save_key('ousama_', vc, str(ctx.author.id), 'game_master')