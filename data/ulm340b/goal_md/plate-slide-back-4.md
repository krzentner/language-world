

The task `plate-slide-side` requires the robot to slide the plate sideways into the target location.
To slide the plate sideways into the target location reliably, what steps the robot should perform?


Now, you have finished learning about all the tasks.  For each task you'll be given 10 test problems to ensure you understand how the task should be done.  You'll only move on to the next task once you've correctly answered 9 of the 10 problems.


"""

def show_tutorial():
    """Shows the tutorial instructions above."""
    instructions = ["Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.",
                    "To push the button down from above reliably, the robot should perform the following steps:",
                    "    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top",
                    "    Because this is \"topdown\", we just need to line up the gripper from above. Line up the robot's gripper from above.",
                    "    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed",
                    "    Now that the gripper is lined up, just push down on the button.",
                    "    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button",
                    "To pull the drawer open reliably, the robot should perform the following steps:",
                    "    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer",
                    "    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.",
                    "    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle",
                    "    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.",
                    "    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle",
                