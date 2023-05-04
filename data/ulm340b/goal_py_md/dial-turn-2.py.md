

Once you've completed the function, type:
```
robot = Robot()
dial_turn(robot)
robot.finish()
```
"""

# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial handle
    #  2. Grab the dial handle with the gripper
    #  3. Turn the dial
    # Put gripper vertically aligned above the dial handle
    if check("the robot's gripper is not vertically aligned with dial handle"):
        robot.move_gripper("vertically aligned with the dial handle")
    # Put the gripper left of the dial handle
    if check("the robot's gripper is not left of the dial handle"):
        robot.move_gripper("left of the dial handle")
    # Rotate the dial handle
    if check("the robot's gripper is left of the dial handle and the robot's gripper is not almost vertically aligned with dial handle"):
        robot.move_gripper("above the dial handle")
    
robot = Robot()
dial_turn(robot)
robot.finish()


# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial handle
    #  2. Grab the dial handle with the gripper
    #  3. Turn the dial
    # If the gripper is not above the dial handle, move the gripper above the
    # dial handle.
    if check("the robot's gripper is not above dial handle"):
        robot.move_gripper("above dial handle")
    # If the gripper is left of the dial handle, move the gripper forward of the
    # dial handle.
    if check("the robot's gripper is left of dial handle"):
        robot.move_gripper("forward of dial handle")
    # If the gripper is forward of the dial handle, then rotate it around dial
    # handle.
    if check("the robot's gripper is forward of dial handle and the robot's gripper is not almost vertically aligned with dial handle"):
        robot.move_gripper("almost vertically aligned with dial handle")

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put