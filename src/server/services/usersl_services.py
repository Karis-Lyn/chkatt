# Covers user authentication (login/signup) within pure business logic
# The models is called by src/server/handlers/
from os import read
from src.server.handlers.user_manage import server
from src.server.utils.read_conf import read_pfile
from src.server.services.usr_facade_service \
import import_shared, bind_cfunction
from ctypes import *

CONFIGURE_FILE = "db_chkatt.json"
CONFIG_MOD_PAH = "src/server/config/"

def register_user():
    dbctrl = import_shared("libdbctrl", "src/server/c_lib/")
    run_mysql = bind_cfunction(dbctrl, "run_mysql", \
    [c_char_p, c_char_p, c_char_p, c_char_p, c_uint64], c_bool)
    db = read_pfile(CONFIGURE_FILE, CONFIG_MOD_PAH)
    if db:
        print(db["host"])
    else:
        print("Error: [not found].")
    #run_mysql()

