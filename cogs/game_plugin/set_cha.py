from random import choice, shuffle
from utils.date import *

load_ousama = load('ousama_')

def set_ousama(ctx):
    vc_id = str(ctx.author.voice.channel.id)
    ousama = choice(load_ousama['list_'])
    load_ousama[str(vc_id)]['ousama_'] = ousama
    load_ousama[str(vc_id)]['list_'].remove(ousama)
    save(load_ousama, 'ousama_')

def shuffle_member(ctx):
    vc_id = str(ctx.author.voice.channel.id)
    shuffle(load_ousama[vc_id]['list_'])
    save(load_ousama, 'ousama_')


def set_member(ctx):
    vc_id = str(ctx.author.voice.channel.id)
    save_key('ousama_', vc_id, {})
    counter = 1
    while True:
        for member in load_ousama[vc_id]['list_']:
            load_ousama[vc_id][str(counter)] = str(member)
            save(load_ousama, 'ousama_')
            counter = counter + 1
        break

def set_main(ctx):
    set_ousama(ctx)
    shuffle_member(ctx)
    set_member(ctx)