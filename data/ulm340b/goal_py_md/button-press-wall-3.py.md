

"""

import time

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from allennlp_demo.common.testing import ModelTestCase


def run_demo():
    with ModelTestCase("allennlp-robot-control", timeout=300) as tester:
        tester.test_model()


def make_window(model_archive, dataset):
    master = tk.Tk()
    master.minsize(width=800, height=300)
    master.maxsize(width=800, height=300)
    master.wm_title("robot controller demo")

    task_instructions = tk.Label(master, text='''
        In the last task, `window-close`, the robot is supposed to push a window closed by pushing on its handle.
        The code to do this is as follows:

        ```
        # window-close: slide the window closed to the right
        def window_close(robot):
            # Steps:
            #  1. Put gripper left of the window handle
            #  2. Start pushing against the window handle to close the window
            #  3. Push the window closed harder
            # If the the window handle is right of the robot's gripper, we should move the
            # gripper near the window handle to start pushing
            if check("the robot's gripper is in front of the window handle"):
                robot.move_gripper("right of the window handle")
            # If the robot's gripper is near the window handle we can probably slide the
            # window close now by moving the gripper right.
            if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
                robot.move_gripper("almost vertically aligned with the window handle")
            # If the robot's gripper is starting to be in front of the window handle,
            # push harder.
            if check("the robot's gripper is near the window handle"):
                robot.move_gripper("forward aligned with the window handle")
        ```

        Your job is to write a program that instructs the robot how to push the button with a short wall in the way.
        To test your program, click the "Test" button.
    ''')
    task_instructions.grid(row=1, column=0, sticky="nsew")
    task_instructions.columnconfigure(0, weight=1)
    task_instructions.rowconfigure(1,