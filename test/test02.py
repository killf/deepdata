from deepdata.cifar import CIFAR10
from deepdata import MNIST, KMNIST, FashionMNIST
import deepdata.urls

# dataset = CIFAR10("data", download=True)

# dataset = MNIST("data", download=True)
dataset = FashionMNIST("data", download=True)
for item in dataset:
    print(item)
