# Recive whole socketio event and verify arguments
# pull the services modules
from src.server.network.ascserver import server
from src.server.services.usersl_services import *

@server.event
def useradd(sid, data):
    if not data: return
    register_user(data)
    print(str(data))

@server.event
def login(sid, data):
    print(str(data))

@server.event
def send_msg(sid, data):
    print(str(data))
