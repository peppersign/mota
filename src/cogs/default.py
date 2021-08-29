#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from datetime import timedelta
from time import time
from os import listdir


class default(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        global uptime
        global commands 
        uptime = time()
        commands = [command for command in self.bot.walk_commands() if command.help != None]


    @commands.command()
    async def ping(self, ctx):
        """Test bot ping"""
        await ctx.send("Pong!")


    @commands.command()
    async def help(self, ctx):
        """Shows this list"""

        commandstr = "\n".join([f"- {x.name:<10}  {x.help}" for x in commands])
        message = f"+ Commands\n----------\n\n{commandstr}"
        await ctx.send(f"""```diff\n{message}```""")
 

    @commands.command()
    async def stats(self, ctx):
        """Server stadistics"""
        embed = discord.Embed(title=f"{ctx.guild.name}'s stats", color=discord.Color.red(), description="***Server stadistics***")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Owner", value=f"```{ctx.guild.owner}```")
        embed.add_field(name="Members", value=f"```{len(ctx.guild.members)}```")
        embed.add_field(name="Uptime", value=f"```{timedelta(seconds=round(time() - uptime))}```")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(default(bot))
