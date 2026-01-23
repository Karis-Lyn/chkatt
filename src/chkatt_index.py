import os
import hashlib as hash
import asyncio as sco
import read_conf as config
from user import c, Client

APP_PROMPT = "chkatt>"
libdbctrl = c.CDLL("libdbctrl.so")

async def asc_input():
    return await sco.get_event_loop().run_in_executor(
            None, input)

async def operate_chat():
    run_mysql = libdbctrl.run_mysql
    run_mysql.argtypes = [
            c.c_char_p, c.c_char_p,
            c.c_char_p, c.c_char_p,
            c.c_uint64
            ]
    run_mysql.restype = c.c_bool

    user_add = libdbctrl.user_add
    user_add.argtypes = [c.c_char_p, c.c_char_p]
    user_add.restype = c.POINTER(Client)

    destory_mysql = libdbctrl.destory_mysql
    destory_mysql.restype = c.c_bool

    print(end="\n")
    code = ""
    salt = None
    key = None
    name = ""
    pwd = None
    
    while code != "quit":
        print(APP_PROMPT, end="")
        code = await asc_input()
        match code:
            case "1":
                # 注册账户，注册成功更换提示符
                data = config.read_pfile("chkatt_db.json", "etc")
                db = ""

                if data is not None:
                    db = data['database']
                    run_mysql(
                    db['host'].encode('utf-8'),
                    db['user'].encode('utf-8'),
                    db['password'].encode('utf-8'),
                    db['database'].encode('utf-8'),
                    int(db['port']))
                
                print("type your user name: ")
                code = await asc_input()
                name = code
                print("type your user password: ")
                code = await asc_input()
                salt = os.urandom(16)
                key = hash.pbkdf2_hmac("sha256", code.encode("utf-8"), salt, 100000, 32)
                
                pwd = f"{key}{salt}"
                user_add(name.encode("utf-8"), pwd.encode("utf-8"))

                destory_mysql()
                #await send_msg()
            case "2":
                # 登录账户，登录成功更换提示符
                print(code)
            case "quit":
                await sio.disconnect()
            case _:
                print(code)
