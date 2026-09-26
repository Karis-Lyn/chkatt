# Covers user authentication (login/signup) within pure business logic
# The models is called by src/server/handlers/
from os import read
from src.server.handlers.user_manage import server
from src.server.utils.read_conf import read_pfile
from src.server.services.usr_facade_service \
import import_shared, bind_cfunction
from src.server.infra.clib import load_api, \
create_string_buffer, c_ubyte, OUTPUT_CALLBACK

CONFIGURE_FILE = "db_chkatt.json"
CONFIG_MOD_PAH = "config"
USER_LEN = 16
SALT_LEN = 32
PWD_LEN = 8

# future change
def connect_to_mysql(config_data):

    if config_data:
        host = config_data["host"].encode("utf-8")
        user = config_data["user"].encode("utf-8")
        pwd = config_data["pwd"].encode("utf-8")
        database = config_data["database"].encode("utf-8")
        port = config_data["port"]
        return host, user, pwd, database, port
    else:
        print("Error: [not found].")
    return None, None, None, None, 0

user_err_output = lambda msg_bytes: \
    print(f'Err: [User name must needs one or more upperletter]')

pwd_err_output = lambda msg_bytes: \
        print(f'Err: [Password must needs one or more @~#$%^&*-_ character]')

def is_valid_user_name(name):
    api = load_api()
    name = name.strip()
    test_reg = "^(?=.*-)[\\w-]{2, 16}$"
    reg = "^(?=.*[A-Z])[\\w-]{2, 16}"
    reg_check_name = reg
    err_msg_byte = "User name must needs one or more upperletter".encode("utf-8")

    if len(name) > USER_LEN: # user name not exceed 16
        print(f"[User Err: User name must not exceed {USER_LEN} characters]")
        return None
    elif not name: # strip
        print("[User Err: You didn't type any character]")
        return None
    # transform to C api
    c_callback = OUTPUT_CALLBACK(user_err_output)
    # verify 
    api.libuser.recheck_usr_data(
            name,
            reg_check_name.encode("utf-8"),
            c_callback)
    return name

def is_valid_pwd(pwd):
    api = load_api()
    pwd = pwd.strip()
    reg_check_pwd = "^(?=.*\\d)(?=.*[a-zA-Z])(?=.*[@~#$%^&*-_]).*"
    err_msg_byte = "Password must needs one or more @~#$%^&*-_ ,\
    letters and number character".encode("utf-8")

    if len(pwd) > PWD_LEN: # pwd not exceed 8
        print(f"[Pwd Err: Password must not exceed {PWD_LEN} characters]")
        return None
    elif not pwd:
        print("[Pwd Err: You didn't type any character]")
        return None
    c_callback = OUTPUT_CALLBACK(pwd_err_output) # transform to C api
    # verify 
    api.libuser.recheck_usr_data(
            pwd,
            reg_check_pwd.encode("utf-8"),
            c_callback)
    return pwd


def register_user(data):
    # define unsigned char
    #uchar_32 = c_ubyte * SALT_LEN
    # psalt = uchar_32()
    salt_buf = create_string_buffer(SALT_LEN)
    hash_buf = (c_ubyte * (SALT_LEN))()

    db = read_pfile(CONFIGURE_FILE, CONFIG_MOD_PAH)
    api = load_api()

    host, user, pwd, database, port = connect_to_mysql(db)
    is_success = api.libdbctrl.run_mysql(host, user, pwd, database, port) # ***
    #Client* user_add(char* nam, char* pwd_key, char* salt)
    # salt = cast(salt_buf, c_char_p)
    api.libuser.gen_salt(salt_buf)
    salt = salt_buf.value

    name = data["usr_name"].encode("utf-8")
    valid_name = is_valid_user_name(name)
    if not valid_name: return 0

    usr_pwd  = data["pwd"].encode("utf-8")
    valid_pwd = is_valid_pwd(usr_pwd)
    if not valid_pwd: return 0

    hash_hex = ""
    # pwd_demo = "1234567".encode("utf-8")
    print(f"name: {valid_name}, pwd: {valid_pwd}")
    if api.libuser.pwd_hash(valid_pwd, salt, hash_buf):
        hash_hex = bytes(hash_buf).hex().encode("utf-8")
        print(f"salt: {salt}")
        print(f"hash: {hash_hex}")
    else:
        print("Error: [not found].")
    # create a new unsigned char* with copy origin value for target varible
    # if (api.libuser.verify_pwd(pwd_demo, salt, stored_raw) == 1): print(1)
    
    # api.libdbctrl.user_add(valid_name, hash_hex, salt)
    # stored_raw = (c_ubyte * 32).from_buffer_copy(bytes.fromhex(hash_hex))
    # api.libuser.verify_pwd(pwd_demo, salt, stored_raw)

def test_input():
    pass
