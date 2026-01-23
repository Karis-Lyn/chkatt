import socketio as s
import asyncio as sco
from chkatt_index import asc_input
from chkatt_index import operate_chat
import os
import ui 

DNS = "localhost"
PORT = "3000"
PORTOCOL = "http://"
SIGN_UP = "1"
LOGIN_IN = "2"

# client
sio = s.AsyncClient()
#libuser = c.CDLL("libuser.so")

@sio.event
async def connect():
    print("success conncet to server")
    ui.welcome_info()
    ui.sign_up_info()

@sio.event
async def resp_msg(data):
    os.system("clear")
    print(f"msg: {data}")
    print("reply: ", end="")

@sio.event
async def disconnect():
    print(f"client was disconnected")
# business code
async def send_msg():
    while True:
        print("send: ", end="")
        msg = await asc_input();
        if msg.strip():
            await sio.emit("receive_msg", msg.strip())



async def main():
    url = f"{PORTOCOL}{DNS}:{PORT}"
    try:
        await sio.connect(url)
        sco.create_task(operate_chat())
        await sio.wait()
        
    except KeyboardInterrupt:
        print("bye~~~")


sco.run(main())
