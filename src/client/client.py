import asyncio as sco
from src.client.network.asclient import client
from src.client.network.index_auth_req import *

DNS = "localhost"
PORT = "3000"
PORTOCOL = "http://"

@client.event
async def responder(data):
    pass

# --------------------------------------------------
async def main():
    url = f"{PORTOCOL}{DNS}:{PORT}"
    methods = {
        "useradd_req": useradd_req,
        "login_req": login_req,
        "send_msg_req": send_msg_req
    }
    try:
        await client.connect(url)
        await idx.operate_chat(methods)
        await client.wait()
        
    except KeyboardInterrupt:
        print("bye~~~")


sco.run(main())
