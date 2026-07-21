from socketio import AsyncClient
from src.client.ui import ui

client = AsyncClient()

@client.event
async def connect():
    print("success conncet to server")
    ui.welcome_info()
    ui.sign_up_info()

@client.event
async def disconnect():
    print(f"client was disconnected")
