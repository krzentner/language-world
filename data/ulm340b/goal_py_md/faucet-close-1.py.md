

You'll also need to add a line to the end of `robot_control_suite` to call the
function.

Make sure to check which statements are false while you write your code.
When you're done, click "Submit". 
 
For your reference, here is an example of a function call:

```
robot_control_suite = {"door-open": door_open, "faucet-close": faucet_close, "push": push}

def door_open(robot):
  if check("the robot's gripper is not almost vertically aligned with door handle"):
      robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
  if check("the robot's gripper is vertically aligned with the door handle"):
      robot.move_gripper("left of the door handle")
```

"""
# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper