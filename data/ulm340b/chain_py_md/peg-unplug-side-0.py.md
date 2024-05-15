

The first thing you'll need is a line to check if the gripper is near the peg.
Since the peg is a long object, instead of checking if the gripper is around the
peg, you should check if it is **forward aligned** with the peg. The way to do
this is to call `check("the robot's gripper is forward aligned with the peg")`.
*/

# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):

/* ## Your program here */

if check("the robot's gripper is not forward aligned with the peg"):
	robot.put("gripper on peg")
if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
	robot.grab("peg")
if check("the robot's gripper is forward aligned with the peg"):
	robot.unplug("peg from hole")
[eod] [code]import os

def is_dir_empty(dirpath):
    """
    check directory is empty or not

    Args:
        dirpath (str): path to directory

    Returns:
        bool: True/False
    """
    return len(os.listdir(dirpath)) == 0


def is_file_exist(filename):
    """
    check file does exist

    Args:
        filename (str): path to file

    Returns:
        bool: True/False
    """
    return os.path.isfile(filename)


def is_dir_exist(dirpath):
    """
    check dir does exist

    Args:
        dirpath (str): path to dir

    Returns:
        bool: True/False
    """
    return os.path.isdir(dirpath)
[eod] [code]"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for