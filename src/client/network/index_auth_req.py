from src.client.network.asclient import client
from src.client.ui import terminal_ui as idx

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

