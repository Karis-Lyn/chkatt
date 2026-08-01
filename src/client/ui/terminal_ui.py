import asyncio as sco

PROMPT_UNAUTH = "chkatt>"
# karis@dev-team:[cht]$
PROMPT_AUTH = ["karis", "@", "dev-team", ":[", "cht", "]", "$"]
STAT_UNAUTH = "chkatt"
STAT_AUTH = "user"
CMD_EXIT = "exit"
NO_BR = ""
QUIT = "\\quit"
HELP = "\\help"

TYPE_USRNAM = "Type your username: "
TYPE_PASSWD = "Type your password: "
CHOOSE_USRNAM = "choose a user: "

COMMAND_MAP = {
        "1": {"func": "useradd_req", "desc": "sign up"},
        "2": {"func": "login_req", "desc": "login in"},
        "3": {"func": "send_msg_req", "desc": "send message"},
}
async def asc_input(prompt=None, br=None):
    if prompt:
        if br is not None:
            print(prompt, end=br)
        else:
            print(prompt)
    return await sco.get_event_loop().run_in_executor(
            None, input)

async def operate_chat(methods):
    cmd = ""
    prompt = ""
    stat = STAT_UNAUTH
    SPROMT_AU = "".join(PROMPT_AUTH)
    while True:
        prompt = SPROMT_AU if stat == STAT_AUTH else PROMPT_UNAUTH

        cmd = await asc_input(prompt=prompt, br=NO_BR)

        if cmd.lower() == CMD_EXIT: break

        new_stat = await manager(cmd, methods, stat)

        if new_stat:
            stat = new_stat




async def manager(code, methods, status):
    target = COMMAND_MAP.get(code)

    if not target:
        print(f"ERR: [invalid command {code}.]")
        return None

    action_fn = methods.get(target["func"])

    if not action_fn:
        print("ERR: [unknown error].]")
        return None

    try:
        await action_fn()

        if status == STAT_UNAUTH and target["func"] in ["login_req", "useradd_req"]:
            # 这里可以做得更严谨，比如根据 action_func 的返回值判断是否登录成功
            print("[*] Operation complete. Switching to authenticated mode...")
            return STAT_AUTH

    except Exception as e:
        print(f"ERR: [Action failed] {e}")


