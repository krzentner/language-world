

#######################

# Instructions end here.
# The task is to write the following lines of code:

# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up the handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above handle"):
        robot.move_gripper("above handle")
    # If the gripper is lined up above the handle we can drop the gripper to
    # close it around the handle.
    if check("the robot's gripper is above handle"):
        robot.move_gripper("around the handle")
    # Now that we have grabbed the handle, we can raise it by closing the gripper.
    if check("the robot's gripper is above handle and the robot's gripper is around the handle"):
        robot.move_gripper("above handle", close_gripper=True)


def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up the handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above handle"):
        robot.move_gripper("above handle")
    # If the gripper is lined up above the handle we can drop the gripper to
    # close it around the handle.
    if check("the robot's gripper is above handle"):
        robot.move_gripper("around the handle")
    # Now that we have grabbed the handle, we can raise it by closing the gripper.
    if check("the robot's gripper is above handle and the robot's gripper is around the handle"):
        robot.move_gripper("above handle", close_gripper=True)
[eod] [code]import datetime
import time

from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from article.models import BlogPost


# Create your views here.
class Index(LoginRequiredMixin, View):
   