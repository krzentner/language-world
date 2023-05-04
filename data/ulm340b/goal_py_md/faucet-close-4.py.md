

and fill in the rest of the code.

Here is a list of some of the possible actions your program can take.
It should be enough for you to fill in the code.
If you need more information, please ask your assistant.
```
#  1. The robot can move its gripper to the left of the faucet.
#  2. The robot can move its gripper above the faucet.
#  3. The robot can move its gripper forward aligned with the faucet.
#  4. The robot can move its gripper near the faucet.
#  5. The robot can move its gripper left of the faucet.
#  6. The robot can move its gripper vertically aligned with the faucet.
```

```
>>> program
```

```
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
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the