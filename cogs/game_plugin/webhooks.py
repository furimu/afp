from discord import Embed, Webhook, AsyncWebhookAdapter
import aiohttp
async def create_webhook(ctx):
    if len(await ctx.channel.webhooks()) != 0:
        for webhoo in await ctx.channel.webhooks():
            return webhoo.url

    else:
        webhoo = await ctx.channel.create_webhook(name = '王様ゲーム', reason = '王様ゲームを始める為のテキストを送信するために作成')
        return webhoo.url

async def send_webhook(ctx, voice_channel, hour, minute, mention):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(await create_webhook(ctx), adapter=AsyncWebhookAdapter(session))
        e = Embed(
            title = f'{voice_channel.name}で{hour}:{minute}に王様ゲームを始めます。',
            description = '参加する方は自分の性別のリアクションを押してください。'
        )
        if mention is None:
            return await webhook.send(username= ctx.author, avatar_url = ctx.author.avatar_url, embed = e)

        else:
            return await webhook.send(','.join(role.mention for role in mention), wait = True, username= str(ctx.author), avatar_url = ctx.author.avatar_url, embed = e)