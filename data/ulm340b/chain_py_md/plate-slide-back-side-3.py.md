

and write code after that to complete the task.

You can find the functions I used in the previous examples in the `a_functions.py`
file, but you may use different functions if you would like.
"""
[eod] [code]import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

use_cuda = torch.cuda.is_available()

train_data = dsets.MNIST(root='./mnist/',
                         train=True,
                         transform=transforms.ToTensor(),
                         download=True)

test_data = dsets.MNIST(root='./mnist/',
                        train=False,
                        transform=transforms.ToTensor())

# use_cuda = torch.cuda.is_available()

batch_size = 100

train_loader = torch.utils.data.DataLoader(dataset=train_data,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_data,
                                          batch_size=batch_size,
                                          shuffle=False)

# define network
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

model = NeuralNet(784, 50, 10)

if use_cuda:
    model.cuda()

optimizer = torch.optim.SGD(model.parameters(), lr=0.003, momentum=0.9)

# define some helper functions to prepare our data
def get_batch(source, cuda=False):
    if cuda:
        data, labels = Variable(source[0]).cuda(), Variable(source[1]).cuda()
    else:
        data, labels = Variable(source[0]), Variable(source[1])
    return data, labels
