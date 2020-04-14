from multiprocessing import Process, Pipe, Value
import time
import os
import random
import numpy as np

__all__ = ["DataLoader"]


class StopGenerator:
    def __init__(self, pid=None):
        self.pid = pid


def default_collate(batch):
    if batch is None or not isinstance(batch, list) or len(batch) == 0:
        return batch

    result = [[] for _ in range(len(batch[0]))]
    for items in batch:
        for idx, item in enumerate(items):
            result[idx].append(item)

    result_cvt = []
    for i in range(len(result)):
        if isinstance(result[i][0], np.ndarray):
            result_cvt.append(np.stack(result[i]))
        elif isinstance(result[i][0], float) or isinstance(result[i][0], int):
            result_cvt.append(np.array(result[i]))
        else:
            result_cvt.append(result[i])

    return tuple(result_cvt)


class DataLoader:
    def __init__(self, generator, batch_size=4, maxsize=32, collate_fn=default_collate, shuffle=False):
        self.generator = generator
        self.batch_size = batch_size
        self.maxsize = maxsize
        self.collate_fn = collate_fn
        self.num_worker = 1
        self.shuffle = shuffle

    def __iter__(self):
        def sample_generator(generator, r, w, count, tid):
            idx_ls = list(range(len(generator)))
            if self.shuffle:
                random.shuffle(idx_ls)

            for i in idx_ls:
                if i % self.num_worker != tid:
                    continue

                while count.value >= self.maxsize:
                    time.sleep(0.02)
                    continue

                w.send(generator[i])
                with count.get_lock():
                    count.value += 1

            w.send(StopGenerator(pid=os.getpid()))
            with count.get_lock():
                count.value += 1

        r, w = Pipe(True)
        count = Value('i', 0)

        process_map = dict()
        for tid in range(self.num_worker):
            process = Process(target=sample_generator, args=(self.generator, r, w, count, tid))
            process.start()
            process_map[process.pid] = process

        def parallel_generator():
            result = []
            while len(process_map) > 0:
                item = r.recv()
                with count.get_lock():
                    count.value -= 1

                if isinstance(item, StopGenerator):
                    del process_map[item.pid]
                    continue

                result.append(item)
                if len(result) >= self.batch_size:
                    if self.collate_fn is not None:
                        result = self.collate_fn(result)

                    yield result
                    result = []

        return parallel_generator()
