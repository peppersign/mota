#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def modtest(self, ctx):
        ctx.send("mod test xd")

            
def setup(bot):
    bot.add_cog(mod(bot))
