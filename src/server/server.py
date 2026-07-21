import asyncio as sco
from aiohttp import web
from src.server.network.ascserver import server


app = web.Application()
server.attach(app)

@server.event
async def receiver(sid, data):
    pass

@server.event
def useradd(sid, data):
    print(str(data))

@server.event
def login(sid, data):
    print(str(data))

@server.event
def send_msg(sid, data):
    print(str(data))

def main():
    if __name__ == "__main__":
        print("The server start to 3000")
        web.run_app(app, host="0.0.0.0", port=3000)

main()
