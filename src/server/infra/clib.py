# This module serves as a compatibility layer that are used to loading and binding C API.
from types import SimpleNamespace
from src.server.services.usr_facade_service import bind_cfunction, import_shared
from ctypes import *

_API = None
C_LIB_PATH = "src/server/c_lib"
OUTPUT_CALLBACK = CFUNCTYPE(None, c_char_p)

BIND_API = {
    "libdbctrl": {
        "user_add": ([c_char_p, c_char_p, c_char_p],
                     c_bool),
        "run_mysql": ([c_char_p, c_char_p, c_char_p, 
                       c_char_p,], c_bool)
    },
    "libuser": {
        "gen_salt": ([c_char_p], c_bool),
        "pwd_hash": ([c_char_p, c_char_p,
                POINTER(c_ubyte)], c_bool),
        "recheck_usr_data": ([c_char_p, c_void_p,
                            OUTPUT_CALLBACK],
                            c_bool)
    }
}

def load_api():
    global _API
    if not _API:
        API = SimpleNamespace()
        for libn, feats in BIND_API.items():
            # shared library instance, if you wanna get the api name, arguments type and return type, you should enumerate the bind_api map.
            single_lib = import_shared(libn, C_LIB_PATH)
            setattr(API, libn, SimpleNamespace())
            # bind_cfunction(db, fn_name, arg_types=, ret_types=)
            for fn_name, (args, ret) in feats.items():
                # setting features name, arguments type and return type to libn of value
                setattr(getattr(API, libn), fn_name, 
                        bind_cfunction(single_lib, fn_name, args, ret))
            
        _API = API
    return _API
