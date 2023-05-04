
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing the window handle to open the window
    #  3. Push the window open harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper to the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper right.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")

[eod] [code]from os.path import join
import os
from torch.utils.tensorboard import SummaryWriter
from config import get_args
from shutil import rmtree
from datasets import get_dataset, get_dataloader
from models import get_model
import logging

logger = logging.getLogger()
if not logger.hasHandlers():
    logger.addHandler(logging.FileHandler('train.log', 'w'))
    logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def train():
    args = get_args()
    args.distributed = False
    # 1. dataset and dataloader
    train_dataset, val_dataset = get_dataset(args.dataset, args.dataset_dir,
                                             train_size=0.8, shuffle=True,
                                             resize=args.resize, augment=True)
    train_dataloader = get_dataloader(train_dataset, batch_size=args.batch_size,
                                      num_workers=args.num_workers,
                                      collate_fn=train_dataset.collate_fn,
                                      shuffle=True)
    val_dataloader = get_dataloader(val_dataset, batch_size=args.batch_size,
                                    num_workers=args.num_