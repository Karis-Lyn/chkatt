from src.server.network.ascserver import server

@server.event
def useradd(sid, data):
    print(str(data))

@server.event
def login(sid, data):
    print(str(data))

@server.event
def send_msg(sid, data):
    print(str(data))
