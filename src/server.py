import socketio as s
from aiohttp import web


sio = s.AsyncServer(async_mode="aiohttp")
app = web.Application()
sio.attach(app)


@sio.event
async def connect(sid, environ):
    print(f"connection successful: {sid}")

@sio.event
async def receive_msg(sid, data):
    await sio.emit("resp_msg", data, skip_sid=sid)

@sio.event
async def disconnect():
    print("disconnected with client", end="\n")

if __name__ == "__main__":
    print("The server start to 3000")
    web.run_app(app, host="0.0.0.0", port=3000)

