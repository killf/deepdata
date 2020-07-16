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

shmid = shmget(SHM_KEY, SHM_SIZE, 0o666)
if shmid < 0:
    print("System not infected")
else:
    addr = shmat(shmid, None, 0)
    s = string_at(addr, SHM_SIZE)
    print(s)
    bs = (c_byte * SHM_SIZE).from_address(addr)

    import numpy as np

    bs = (c_byte * SHM_SIZE).from_address(addr)
    a = np.ndarray((4, 4), buffer=bs)
    print(a)
