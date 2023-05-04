

Here are the steps:
- Move the gripper above the handle.
- Drop the gripper around the handle.
- Pull the drawer open.

Please write your program in the box below.
"""

code = """
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull drawer open

    # Move the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.move("gripper above drawer handle")

    # If the gripper is above the handle and open, put the gripper around the handle.
    if check("the robot's gripper is above the drawer handle and the robot's gripper is open"):
        robot.drop("gripper around the drawer handle")
    
    # As long as the gripper is lined up with the handle, we can keep pulling.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("the drawer open")

"""[eod] [code]import pandas as pd

from utils import *


def make_df(path, delim=','):
    """
    The function to make pandas dataframe from a text file.
    :param path: path of the text file
    :param delim: delimiter (default: ,)
    :return: pandas dataframe
    """
    return pd.read_csv(path, sep=delim)


def df_split(df):
    """
    The function to split a pandas dataframe into 3 (data_x, data_y, data_z)
    :param df: pandas dataframe (a time series data)
    :return: pandas dataframes (data_x, data_y, data_z)
    """
    m = len(df)
    N = 12
    data_x = pd.DataFrame()
    data_y = pd.DataFrame()
    data_z = pd.DataFrame()

    for i in range(0, m - N):
        tmp = df[i:i + N, 1:]
        index = df[i:i + N].index
        data_x = data_x.append(tmp[1:3])
        data_