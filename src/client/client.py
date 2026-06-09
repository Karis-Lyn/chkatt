import socketio as s
import asyncio as sco
from src.client.ui import ui
from src.client.ui import chkatt_index as idx

DNS = "localhost"
PORT = "3000"
PORTOCOL = "http://"

# client
client = s.AsyncClient()

@client.event
async def connect():
    print("success conncet to server")
    ui.welcome_info()
    ui.sign_up_info()

@client.event
async def responder(data):
    pass

@client.event
async def disconnect():
    print(f"client was disconnected")

# --------------------------------------------------
def useradd_req():
    print("hello")

def login_req():
    print(1)

def send_msg_req():
    print(2)

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
