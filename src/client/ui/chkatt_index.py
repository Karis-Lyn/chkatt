import asyncio as sco

APP_PROMPT = "chkatt>"
NO_BR = ""
QUIT = "\\quit"
HELP = "\\help"
stat = "chkatt"
SIGN_UP = "1"
LOGIN_IN = "2"
SEND_MSG = "3"

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
    code = ""
    while is_quit != QUIT:
        code = await asc_input(APP_PROMPT, NO_BR)
        manager(code, methods)




def manager(code, methods):
    match code:
        case "1":
            methods["useradd_req"]()
        case "2":
            methods["login_req"]()
        case "3":
            methods["send_msg_req"]()
        case _:
            pass

