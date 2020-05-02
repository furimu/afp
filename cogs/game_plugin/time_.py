from utils.date import *

load_ousama = load('ousama_')

async def check_time(vc, minute: str, hour: str = None):

    if not load_file[vc].get('minute'):
        load_ousama[vc]['minute'] = minute
        save(load_ousama, 'ousama')

    if not load_ousama[vc].get('hour'):
        load_ousama[vc]['hour'] = hour
        save(load_ousama, 'ousama')
    else:
        return await ctx.send('既にそのチャンネルでは王様ゲームが開始されています。')

async def check_times(time_):
    if not time_:
        return await ctx.send('時間が指定されてません。')