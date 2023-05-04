
"""[eod] [code]from __future__ import absolute_import

import json
import os

import torch
from torch.utils.data import Dataset
from torchvision import datasets, transforms


class DatasetCollector(object):

    @staticmethod
    def collect_dataset(dataset):
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])
        trainset = datasets.CIFAR10(root='./data', train=True,
                                    download=True, transform=transform)
        testset = datasets.CIFAR10(root='./data', train=False,
                                   download=True, transform=transform)

        if isinstance(dataset, str):
            if dataset == 'train':
                return trainset
            if dataset == 'test':
                return testset

        trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                                  shuffle=True, num_workers=2)
        testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                                 shuffle=False, num_workers=2)
        return trainloader, testloader

    @staticmethod
    def collect_dataset_for_cifar100(dataset):
        trainset = datasets.CIFAR100(root='./data', train=True,
                                     download=True, transform=None)
        testset = datasets.CIFAR100(root='./data', train=False,
                                    download=True, transform=None)

        trainset = Dataset(trainset.train_data, trainset.train_labels,
                           transform=torchvision.transforms.Compose([
                               torchvision.transforms.RandomHorizontalFlip(),
                               torchvision.transforms.RandomCrop(
                                   (32, 32), padding=4),
                               torchvision.transforms.RandomRotation((-20, 20)),
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize((0.5, 0.5, 0.5),
                                                                (0.5, 0.5, 0.5)),
                           ]))
        testset = Dataset(testset.test_data, testset.test_labels,
                          transform=torchvision.transforms.Compose([
                