from utils.date import *
load_ousama = load('ousama_')
async def check_mute(ctx):
    muter = []
    for vc in ctx.channel.guild.voice_channels:
        if not load_ousama.get(str(vc.id)):
            continue
            
        for member in load_ousama[str(vc.id)]['list_']:
            member = ctx.channel.guild.get_member(int(member))

            if member.voice is None:
                continue

    
            if member.voice.self_mute:
                muter.append(member.id)
                await ctx.send(f'{"さん,".join(ctx.channel.guild.get_member(member).mention for member in muter)}さんがミュートの為ゲームを開始する事が出来ません。')
                return True
            else:

                return False


async def check_join_voice_channel(ctx):
    not_member = []
    for vc in ctx.channel.guild.voice_channels:
        if not load_ousama.get(str(vc.id)):
            continue
        
        for member in load_ousama[str(vc.id)]['list_']:
            member = ctx.channel.guild.get_member(int(member))

            if member not in ctx.channel.author.voice.channel.members:
                load_ousama[str(vc.id)]['list_'].remove(str(member.id))
                save(load_ousama, 'ousama_')
                not_member.append(member.id)

    if len(not_member) == 0:
        await ctx.send('f')
        return False
    await ctx.send('さん,'.join(ctx.guild.get_member(member).mention for member in not_member))
    await ctx.send('はボイスチャンネルに参加していないため除外されました。')
    await ctx.send('再参加するには')
    await ctx.send('afp:王様ゲーム+ 参加')
    await ctx.send('を入力してください。')
    return True


