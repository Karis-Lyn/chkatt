import os
import hashlib as hash
import asyncio as sco
import read_conf as config
from user import c, Client

APP_PROMPT = "chkatt>"
libdbctrl = c.CDLL("libdbctrl.so")

async def asc_input(tips):
    print(tips)
    return await sco.get_event_loop().run_in_executor(
            None, input)

