from discord import Embed
from utils.date import *

load_ousama = load('ousama_')

def send_number(ctx):
    vc = str(ctx.author.voice.channel.id)
    e = Embed(
        title = '王様ゲーム番号一覧',
        colour = ctx.author.color
    )
    for k, v, in load_ousama[vc].items():
        if k == 'list' or 'ousama_' or 'minute' or 'hour':
            continue

        e.add_field(
            name = k,
            value = ctx.guild.get_member(int(v)).mention,
            inline = False
        )

    e.set_author(
        text = '指定された番号の人は命令を実行してください。'
    )

    return e