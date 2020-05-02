from random import choice, shuffle
from utils.date import *

load_ousama = load('ousama_')

def set_ousama(ctx):

    for vc in ctx.guild.voice_channels:
        if not load_ousama.get(str(vc.id)):
            continue

        ousama = choice(load_ousama[str(vc.id)]['list_'])
        load_ousama[str(vc.id)]['ousama_'] = ousama
        load_ousama[str(vc.id)]['list_'].remove(ousama)
        save(load_ousama, 'ousama_')

def shuffle_member(ctx):
    for vc in ctx.guild.voice_channels:
        if not load_ousama.get(str(vc.id)):
            continue
    shuffle(load_ousama[str(vc.id)]['list'])
    save(load_ousama, 'ousama_')

    