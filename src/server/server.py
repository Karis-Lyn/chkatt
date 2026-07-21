import asyncio as sco
from aiohttp import web
from src.server.services.index_usr_service import server


app = web.Application()
server.attach(app)

@server.event
async def receiver(sid, data):
    pass


def main():
    if __name__ == "__main__":
        print("The server start to 3000")
        web.run_app(app, host="0.0.0.0", port=3000)

main()
