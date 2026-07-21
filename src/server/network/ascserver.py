from socketio import AsyncServer

server = AsyncServer()

@server.event
async def connect(sid, environ):
    print(f"connection successfull: {sid}")

@server.event
async def disconnect(sid):
    print("disconnected with client", end="\n")
