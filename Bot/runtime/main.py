import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

# @bot.slash_command(name="ban", description="")


def load_blacklist():
    with open('blacklist.txt', 'r') as file:
        return [int(line.strip()) for line in file]


def save_blacklist(blacklist):
    with open('blacklist.txt', 'w') as file:
        file.write('\n'.join(map(str, blacklist)))


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command(name='add_blacklist', hidden=True)
async def add_blacklist(ctx, user_id: int):
    if ctx.author.id == ctx.guild.owner_id:
        blacklist = load_blacklist()
        if user_id not in blacklist:
            blacklist.append(user_id)
            save_blacklist(blacklist)
            await ctx.send(f'Added user {user_id} to the blacklist.')
        else:
            await ctx.send('User is already in the blacklist.')
    else:
        await ctx.send('Only the server owner can add users to the blacklist.')

# Command: Remove a user from the blacklist
@bot.command(name='remove_blacklist', hidden=True)
async def remove_blacklist(ctx, user_id: int):
    if ctx.author.id == ctx.guild.owner_id:
        blacklist = load_blacklist()
        if user_id in blacklist:
            blacklist.remove(user_id)
            save_blacklist(blacklist)
            await ctx.send(f'Removed user {user_id} from the blacklist.')
        else:
            await ctx.send('User is not in the blacklist.')
    else:
        await ctx.send('Only the server owner can remove users from the blacklist.')

# Event: Check if a user is blacklisted before allowing commands
@bot.check
async def is_blacklisted(ctx):
    blacklist = load_blacklist()
    return ctx.author.id not in blacklist


# Run the bot with your token
bot.run('MTEyNDY1NTgxNTc2NTI3NDc1NQ.GoYqPC.CBEWZ9iVrr9aIBL0_D8y1wSKDA1ncDe7NvxlGM')
