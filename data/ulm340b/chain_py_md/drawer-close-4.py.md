


### END TASK
"""

# def drawer_close(robot):
#     # Steps:
#     #  1. Put gripper above drawer handle
#     #  2. Drop gripper around drawer handle
#     #  3. Push closed the drawer
#     # We need to put the gripper above the drawer handle before we can grab it,
#     # because of the angle of the robot's gripper.
#     if check("the robot's gripper is not vertically aligned with drawer handle"):
#         robot.put("gripper above drawer handle")
#     # Once the gripper is lined up above the drawer handle, we should be able to
#     # grab the drawer handle by moving the gripper down around it.
#     if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
#         robot.put("gripper around drawer handle")
#     # Once the gripper is around the drawer handle, we can just push the drawer
#     # close.
#     if check("the robot's gripper is around drawer handle"):
#         robot.push("towards drawer")
[eod] [code]import numpy as np
import cv2
import random
import os
import shutil
import pandas as pd
from glob import glob
from tqdm import tqdm
import argparse

# python3 data/split_data.py --output output/

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str)
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for dataset in ['train', 'test']:
        for image_dir in glob('data/image_set_2/*.jpg'):
            image_dir = os.path.basename(image_dir).split('.jpg')[0]
            output_dir = os.path.join(args.output, dataset, image_dir)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            for input_file in glob(f'data/{image_dir}/*.txt'):
                output_file = os.path.basename(input_file).split('.txt')[0]
                shutil.copy(input_file, f'{output_dir}/{output_file}')

    np.random