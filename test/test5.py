import numpy as np
from multiprocessing import Array, Process
import ctypes
import time

a = np.zeros(shape=(128, 3, 1024, 1024))

np.save("/dev/shm/a", a)
