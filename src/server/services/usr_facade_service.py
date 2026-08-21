from ctypes import *
from typing import Any
from src.server.handlers.user_manage import server

def init():
    pass

def import_shared(lib_name, lib_pth="."):
    import os
    WIN_DB = ".dll"
    WIN_OS = "nt"
    LINUX_DB = ".so"
    LINUX_OS = "posix"

    if os.name == LINUX_OS:
        suffix = LINUX_DB
    elif os.name == WIN_OS:
        suffix = WIN_DB
    else:
        raise OSError(f"Unsupported OS: (os.name)")
    
    full_path = os.path.join(lib_pth, f"{lib_name}{suffix}")
    return CDLL(full_path)


def bind_cfunction(db, fn_name, arg_types=None, ret_types: Any=c_void_p):
    try:
        func = getattr(db, fn_name)
    except AttributeError:
        raise ValueError(f"Not found function: {fn_name} in shared library")

    if arg_types is not None:
        func.argtypes = arg_types

        func.restype = ret_types
    return func
