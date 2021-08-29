#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from colors import *
import sys


def log(msg: str, status: str) -> str:
    timestamp = datetime.now().strftime("%H:%M:%S")
    stats = {
        "INFO": LCYAN,
        "WARN": LYELLOW,
        "ERROR": LRED
       } 

    return print(f"{LBLACK}({timestamp}) [ {stats.get(status) + status}{LBLACK} ] {WHITE + msg}")

