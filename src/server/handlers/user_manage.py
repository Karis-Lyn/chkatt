# Recive whole socketio event and verify arguments
# pull the services modules
from src.server.network.ascserver import server
from src.server.services.usersl_services import *

@server.event
def useradd(sid, data):
    register_user()
    print(str(data))

@server.event
def login(sid, data):
    print(str(data))

@server.event
def send_msg(sid, data):
    print(str(data))
