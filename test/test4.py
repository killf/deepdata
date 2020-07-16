import numpy as np
from deepdata import FashionMNIST, DataLoader, Dataset


class MyDataset:
    def __len__(self):
        return 10240

    def __getitem__(self, item):
        return np.ones(shape=(3, 1024, 1024))


dataset = MyDataset()
data_loader1 = DataLoader(dataset, batch_size=32, num_worker=4)
for images in data_loader1:
    print(images.shape)

# from torch.utils.data import DataLoader
#
# data_loader2 = DataLoader(dataset, batch_size=32, num_workers=4)
# for images in data_loader2:
#     print(images.shape)
