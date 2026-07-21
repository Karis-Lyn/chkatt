import asyncio as sco
from src.client.ui import chkatt_index as idx
from src.client.network.asclient import client

DNS = "localhost"
PORT = "3000"
PORTOCOL = "http://"

@client.event
async def responder(data):
    pass

# --------------------------------------------------
async def useradd_req():
    usr_data = {}
    name = await idx.asc_input(idx.TYPE_USRNAM, "")
    pwd = await idx.asc_input(idx.TYPE_PASSWD, "")
    usr_data["usr_name"] = name
    usr_data["pwd"] = pwd
    await client.emit("useradd", usr_data)

async def login_req():
    name = await idx.asc_input(idx.TYPE_USRNAM, "")
    pwd = await idx.asc_input(idx.TYPE_PASSWD, "")

async def send_msg_req():
    name = await idx.asc_input(idx.CHOOSE_USRNAM, "")

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
