import socketio as s
import asyncio as sco
from aiohttp import web


server = s.AsyncServer(async_mode="aiohttp")
app = web.Application()
server.attach(app)


@server.event
async def connect(sid, environ):
    print(f"connection successful: {sid}")

@server.event
async def disconnect(sid):
    print("disconnected with client", end="\n")

@server.event
async def receiver(sid, data):
    pass

@server.event
def useradd(sid, data):
    pass

@server.event
def login(sid, data):
    pass

@server.event
def send_msg(sid, data):
    pass

def main():
    if __name__ == "__main__":
        print("The server start to 3000")
        web.run_app(app, host="0.0.0.0", port=3000)

main()
