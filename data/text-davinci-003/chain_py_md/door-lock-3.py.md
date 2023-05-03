

Steps:
1. Put gripper above dial
2. Drop gripper around dial
3. Turn the dial to the right
4. Release the dial

If the robot's gripper is not above the dial, move it to the dial.
```
# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Turn the dial to the right
    #  4. Release the dial

    # If the robot's gripper is not above the dial, move it to the dial.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # Now that the gripper is above the dial, drop it around the dial to start 
    # turning it.
    if check("the robot's gripper is above the dial and the robot's gripper is not around dial"):
        robot.drop("gripper around dial")
    # Now that the gripper is around the dial, turn it to the right.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial clockwise")    
    # Once the dial is turned, release it.
    if check("the dial is turned to the right"):
        robot.release("dial")