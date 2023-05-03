

Here's the code:
```
# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper next to door dial
    #  2. Rotate dial counter-clockwise
    #  3. Lock dial in place
    # Begin by putting the gripper near the door dial.
    if check("the robot's gripper is not near the door dial"):
        robot.move("gripper to dial")
    # Rotate the dial counter-clockwise.
    if check("the robot's gripper is near the door dial"):
        robot.rotate("counter-clockwise")
    # If the door dial is still moving, put more force direct the dial to
    # lock it in place.
    if check("the door dial is not locked"):
        robot.rotate("counter-clockwise harder")
```