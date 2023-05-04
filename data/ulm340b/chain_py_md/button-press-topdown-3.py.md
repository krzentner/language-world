

I recommend starting by breaking the task into smaller parts, then
focusing on the smaller parts separately.
'''

def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper into the button
    #  3. Slide gripper away from button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # Once the robot's gripper is above the button we can press the button.
    if check("the robot's gripper is above button"):
        robot.push("the button")
    # Move the gripper away so we don't hold the button down.
    if check("the robot's gripper is above button"):
        robot.slide("gripper away from button")

print(button_press_topdown.__doc__)
[eod] [code]import os
from datetime import datetime

import torch
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.optim.lr_scheduler import CosineAnnealingWarmRestarts, ExponentialLR, MultiStepLR, OneCycleLR, ReduceLROnPlateau, StepLR
from torch.utils.data.distributed import DistributedSampler
from torch.utils.tensorboard import SummaryWriter

from config import Configuration
from model import Model
from optimizer import Optimizer
from scheduler import Scheduler
from utils import save_checkpoint, load_checkpoint, mkdir, setup_train_log


def train(config, mode=0, train_dataloader=None, val_dataloader=None):
    """
    :param config: config to train
    :param mode: 0: train, 1: test, 2: test and save
    :param train_dataloader: train dataloader
    :param val_dataloader: val dataloader
    :return:
    """
    mkdir(config.train.model_dir)
    mkdir(config.train.logs_dir)

    if torch.cuda.is_available():
        device = 'cuda'
    else:
        device = 'cpu'

    if config.train.n_gpu > 1:
        ddp_model = DDP(
            Model(config),
            device_ids=[config.train.local_rank],
            output_device=config.train.local_rank
        )
    else: