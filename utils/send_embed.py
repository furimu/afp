from discord import Embed
def defemb(ctx, desc: str):
    embed = Embed(
        description = desc,
        colour = ctx.author.color
    )
    return embed