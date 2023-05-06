import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
#replace with bot token
token = 'token'




#changed?
@bot.event
async def on_ready():
    #sets bot status
    game = discord.Game("with the loopy loops")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('ASCA is now Online <3')

#haha ping pong
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def r(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()

@bot.command()
async def hello(ctx):
    await ctx.send(f'hello {ctx.author.mention} !')

#hehe cutesy commands tehheheheheh
@bot.command()
async def hugazca(ctx):
    cutesy = [f"aww! Thank you {ctx.author.mention}", "other response here i cant think of anything"]
    await ctx.send(random.choice(cutesy))

@bot.command()
async def kissazca(ctx):
    mwah = [f"aww! Thank you {ctx.author.mention}", f"{ctx.author.mention} stoppp"]
    await ctx.send(random.choice(mwah))

#PDA?? (make list of gifs)
@bot.command()
async def kiss(ctx, *, arg):
    await ctx.send(f"{ctx.author.mention} kissed {arg} !!")
    kisslist = ['https://tenor.com/view/anime-kiss-love-mwah-gif-16687888',
                'https://tenor.com/view/kiss-couple-girl-anime-royalmale-gif-25253867',
                'https://tenor.com/view/val-ally-kiss-sweet-cute-love-gif-24939900',
                'https://tenor.com/view/kiss-gif-26359768',
                'https://tenor.com/view/gay-tall-kiss-kisses-school-couple-gif-5517753',
                'https://tenor.com/view/zyrexzeramrt-gif-25803043']
    await ctx.send(random.choice(kisslist))

@bot.command()
async def hug(ctx, *, arg):
    await ctx.send(f"{ctx.author.mention} hugged {arg} !!")
    huglist = ['https://tenor.com/view/yurionice-viktorx-yuri-gay-hugs-anime-gif-17523613',
               'https://tenor.com/view/cute-gay-sleeping-together-gif-13164049',
               'https://tenor.com/view/enage-kiss-anime-hug-kisara-gif-26118528',
               'https://tenor.com/view/alice-vt-gif-25825873',
               'https://tenor.com/view/engage-kiss-anime-hug-gif-26231405',
               'https://tenor.com/view/anime-aesthetic-gif-20913817']
    await ctx.send(random.choice(huglist))

#im lazy
@bot.command()
async def clist(ctx):
    await ctx.send("embed soon :<")

@bot.command()
async def rplaylist(ctx):
    playlists = ['add playlists here']
    await ctx.send(random.choice(playlists))

@bot.command()
async def gm(ctx):
    await ctx.send("Goodmorning Everyone!")
    await ctx.send('https://tenor.com/view/good-morning-anime-cute-kawaii-gif-13979444')
    await ctx.message.delete()

#replace userid with your personal UserID
@bot.command()
async def meds(ctx):
    if ctx.author.id == userid:
        await ctx.send(f'meds taken! good job!')

    else:
        await ctx.send('youre not az.')



bot.run(token)
