import asyncio as sco
from re import U

PROMPT_UNAUTH = "chkatt>"
# karis@dev-team:[cht]$
promtp_auth = ["karis", "@", "dev-team", ":[", "cht", "]", "$"]
NO_BR = ""
QUIT = "\\quit"
HELP = "\\help"
stat = "chkatt"
SIGN_UP = "1"
LOGIN_IN = "2"
SEND_MSG = "3"
TYPE_USRNAM = "Type your username: "
TYPE_PASSWD = "Type your password: "
CHOOSE_USRNAM = "choose a user: "

async def asc_input(prompt=None, br=None):
    if prompt:
        if br is not None:
            print(prompt, end=br)
        else:
            print(prompt)
    return await sco.get_event_loop().run_in_executor(
            None, input)

async def operate_chat(methods):
    is_quit = ""
    DMODE = "chkatt"
    UMODE = "user"
    status = UMODE#DMODE
    cmd = ""
    while is_quit != QUIT:
        cmd = await asc_input(PROMPT_UNAUTH, NO_BR)
        if cmd == LOGIN_IN: status = UMODE
        elif cmd == "exit": status = DMODE
        else: return

        if status == UMODE:
            cmd = await asc_input("".join(promtp_auth), NO_BR)
        elif status == DMODE:
            cmd = await asc_input(PROMPT_UNAUTH, NO_BR)

        await manager(cmd, methods)




async def manager(code, methods):
    match code:
        case "1":
            await methods["useradd_req"]()
        case "2":
            await methods["login_req"]()
        case "3":
            await methods["send_msg_req"]()
        case _:
            pass

