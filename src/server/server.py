# this root module is used to assemble various sub-modules also http server is here
# for example, server/utils, server/models, server/handlers
# server/services, server/network
import asyncio as sco
from aiohttp import web
# must import user_manage in handlers module
# because it is the first module that init the server instance 
# if you import network/ascserver.py of server, it will not run
from src.server.handlers.user_manage import server



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
