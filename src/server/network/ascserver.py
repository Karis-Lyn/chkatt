# chaktt app of server source
# socketio event such as connect and disconnect in here 
# initialize server instance

from socketio import AsyncServer
# expose a server instance to other module
server = AsyncServer()

@server.event
async def connect(sid, environ):
    print(f"connection successfull: {sid}")

@server.event
async def disconnect(sid):
    print("disconnected with client", end="\n")
