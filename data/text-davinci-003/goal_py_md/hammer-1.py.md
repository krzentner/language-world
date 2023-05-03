

The robot needs to hit the nail with the hammer. To do this, it must first line up the hammer above the nail, then rotate the gripper so that it holds the hammer in the proper position, hit the nail, and then release the hammer.

To begin, the robot must line up the gripper above the nail. It can do this by moving the gripper to be vertically aligned with the nail.

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Line up the gripper above the nail
    #  2. Rotate the gripper so it is holding the hammer
    #  3. Hit the nail with the hammer
    #  4. Release the hammer
    
    # Line up the robot's gripper with the nail from above.
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail", close_gripper=True)

```

Once the gripper is vertically aligned with the nail, the robot must rotate it so that it is holding the hammer. To do this, it can move the gripper forward and close it to hold the hammer.

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Line up the gripper above the nail
    #  2. Rotate the gripper so it is holding the hammer
    #  3. Hit the nail with the hammer
    #  4. Release the hammer
    
    # Line up the robot's gripper with the nail from above.
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail", close_gripper=True)
        
    # Rotate the gripper so that it is holding the hammer.
    if check("the robot's gripper is vertically aligned with the nail and is not forward aligned with the nail"):
        robot.move_gripper("forward aligned with the nail", close_gripper=True)
```

Now that the robot has the hammer in hand, it can hit the nail. To do this, it can motion the gripper back and forth quickly a few times to hit the nail.

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Line up the gripper above the nail
    #  2. Rotate the gripper so it is holding the hammer
    #  3. Hit the nail with the hammer
    #