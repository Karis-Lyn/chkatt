import ctypes as c
class User(c.Structure):
    _fields_ = [
        ("usr_nam", c.c_char * 8),
        ("usr_pwd", c.c_char * 16),
        ("stat", c.c_int)
        ]

class Client(c.Structure):
    _fields_ = [
        ("usr", User),
        ("stat", c.c_int8)
        ]


