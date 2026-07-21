import asyncio as sco

APP_PROMPT = "chkatt>"
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
    code = ""
    while is_quit != QUIT:
        code = await asc_input(APP_PROMPT, NO_BR)
        await manager(code, methods)




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

