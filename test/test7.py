from ctypes import *

SHM_SIZE = 4096
SHM_KEY = 67483

try:
    rt = CDLL('librt.so')
except:
    rt = CDLL('librt.so.1')

shmget = rt.shmget
shmget.argtypes = [c_int, c_size_t, c_int]
shmget.restype = c_int

shmat = rt.shmat
shmat.argtypes = [c_int, POINTER(c_void_p), c_int]
shmat.restype = c_void_p

shmctl = rt.shmctl
shmctl.argtypes = [c_int, c_int, POINTER(c_void_p)]
shmctl.restype = c_int

IPC_CREAT = 0o1000
IPC_EXCL = 0o2000
IPC_NOWAIT = 0o4000

IPC_RMID = 0
IPC_SET = 1
IPC_STAT = 2
IPC_INFO = 3

shmid = shmget(SHM_KEY, SHM_SIZE, 0o666 | IPC_CREAT)
if shmid > 0:
    print(f"Create a shared memory segment {shmid}")
else:
    ret = shmctl(SHM_KEY, IPC_RMID, None)
    print(f"Delete exist {SHM_KEY}:{ret}")

# 5177360

addr = shmat(shmid, None, 0)
if addr < 0:
    print(f"addr:{addr}")

import numpy as np

# c_buffer
bs = (c_byte * SHM_SIZE).from_address(addr)
s = np.ndarray((4, 4), buffer=bs)
s.fill(5)

print(type(s))
