"""
Bot by Cora. October 21 2021. 

Will unban the entire ban list.

Thanks to: https://www.codegrepper.com/code-examples/python/discord.py+unban+command for some help with the discord api
"""
import discord,os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
@commands.has_permissions(ban_members=True)
async def test(ctx, arg):
     await ctx.send(arg)

@commands.has_permissions(ban_members=True) # only people w/ ban privileges can use this command
@bot.command()
async def unban(ctx):
    count = 0
    write = True # flag for adding to a text file called "unbanned" the names of the users unbanned
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        count += 1
    await ctx.channel.send(f"Unbanned {count} members") # sends message w/ number of people unbanned
    
    if(write):
        with open('unbanned.txt', 'a') as f:
            for user in banned_users:
                f.write('\n')
                f.write(str(user.user))

   

TOKEN = "Your Token here"  
bot.run(TOKEN)
