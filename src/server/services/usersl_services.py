# Covers user authentication (login/signup) within pure business logic
# The models is called by src/server/handlers/
from os import read
from src.server.handlers.user_manage import server
from src.server.utils.read_conf import read_pfile
from src.server.services.usr_facade_service \
import import_shared, bind_cfunction
from ctypes import *

CONFIGURE_FILE = "db_chkatt.json"
CONFIG_MOD_PAH = "config"
SALT_LEN = 32

def register_user(data):
    dbctrl = import_shared("libdbctrl", "src/server/c_lib/")
    user = import_shared("libuser", "src/server/c_lib/")

    run_mysql = bind_cfunction(dbctrl, "run_mysql", \
    [c_char_p, c_char_p, c_char_p, c_char_p, c_uint64], c_bool)

    # define unsigned char
    #uchar_32 = c_ubyte * SALT_LEN
    # psalt = uchar_32()
    salt_buf = create_string_buffer(SALT_LEN)
    hash_buf = (c_ubyte * (SALT_LEN))()

    gen_salt = bind_cfunction(user, "gen_salt", \
            [c_char_p], c_bool)

    pwd_hash = bind_cfunction(user, \
            "pwd_hash",
          [c_char_p, c_char_p, POINTER(c_ubyte)],
            c_bool)

    user_add = bind_cfunction(dbctrl, "user_add", \
            [c_char_p, c_char_p, c_char_p], c_bool)

    verify_pwd = bind_cfunction(user,
             "verify_pwd",
            [c_char_p, c_char_p, POINTER(c_ubyte)],
            c_bool)

    db = read_pfile(CONFIGURE_FILE, CONFIG_MOD_PAH)
    if db:
        host = db["host"].encode("utf-8")
        user = db["user"].encode("utf-8")
        pwd = db["pwd"].encode("utf-8")
        database = db["database"].encode("utf-8")
        port = db["port"]
        is_success = run_mysql(host, user, pwd, database, port) # ***
        #Client* user_add(char* nam, char* pwd_key, char* salt)
        # salt = cast(salt_buf, c_char_p)
        gen_salt(salt_buf)
        salt = salt_buf.value
        name = data["usr_name"].encode("utf-8")
        usr_pwd  = data["pwd"].encode("utf-8")
        hash_hex = ""
        # pwd_demo = "1234567".encode("utf-8")


        if pwd_hash(usr_pwd, salt, hash_buf):
            hash_hex = bytes(hash_buf).hex().encode("utf-8")
            print(f"salt: {salt}")
            print(f"hash: {hash_hex}")
        else:
            print("Error: [not found].")
        # user_add()
        # create a new unsigned char* with copy origin value for target varible
        # if (verify_pwd(pwd_demo, salt, stored_raw) == 1): print(1)
        
        user_add(name, hash_hex, salt)
        # stored_raw = (c_ubyte * 32).from_buffer_copy(bytes.fromhex(hash_hex))
        # verify_pwd(pwd_demo, salt, stored_raw)
    else:
        print("Error: [not found].")
