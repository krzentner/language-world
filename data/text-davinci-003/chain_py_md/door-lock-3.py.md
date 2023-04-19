

The program will be: 
``` 
# door-lock: turn the dial on the door
#def door_lock(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Turn dial to the desired position
    # First, put the gripper roughly above the dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    # Once the gripper is lined up above the dial, we should be able to
    # grab the dial by moving the gripper down around it.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # Once the gripper is around the dial, turn dial to the desired position.
    if check("the robot's gripper is around dial"):
        robot.turn("dial to desired position")
```