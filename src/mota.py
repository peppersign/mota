#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing
import discord
from log import log
from json import load
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
mota = commands.Bot(command_prefix='.', intents=intents, help_command=None)

extensions = [
        "cogs.default"
]


def load_extensions(*args) -> None:
    for ext in args:
        mota.load_extension(ext)


def read_token() -> str:
    with open("../config.json", 'r') as file:
        config = load(file) 
        return config["token"]


@mota.event
async def on_ready():
    log("Mota is online and ready for use", "INFO")
    

def main() -> None:
    try:
        load_extensions(*extensions)
        mota.run(read_token())

    except discord.errors.LoginFailure:
        log("Invalid token", "ERROR")

    except Exception as error:
        log(f"Exception raised: {error}", "ERROR")


if __name__ == '__main__':
    main()
