
"""

[eod] [code]from . import tools
from . import utils
from .data import DataSet
from .train import train
from .inference import inference


def load_test_dataset():
    train_dataset = DataSet("./data/training")
    test_dataset = DataSet("./data/testing")

    train_dataset.preprocess_images()
    test_dataset.preprocess_images()

    train_dataset.create_datafiles()
    test_dataset.create_datafiles()


def train_network():
    print("TRAINING STARTS")

    train("data/training/train.csv", "data/testing/test.csv")

    print("TRAINING ENDS")


def test_network():
    print("TESTING STARTS")

    image = utils.read_image("data/testing/images/001.png")
    inference(image)

    print("TESTING ENDS")


def generate_training_dataset():
    tools.extract_training_data("data/training")


def generate_testing_dataset():
    tools.extract_testing_data("data/testing")


def test_image_read():
    image = utils.read_image("data/testing/images/001.png")
    utils.show_image(image)


def main():
    # generate_training_dataset()
    # generate_testing_dataset()
    load_test_dataset()
    # train_network()
    test_network()
    # test_image_read()


if __name__ == "__main__":
    main()
[eod] [code]"""
WSGI config for djangoapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoapi.settings')

application = get_wsgi_application()
[eod] [code]from os.path import abspath, dirname, join

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_digits, fetch_lfw_people, fetch_olivetti_faces, fetch_20newsgroups