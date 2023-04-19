

Here's the program:

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper near the dial
    #  2. Place gripper on the dial
    #  3. Turn the dial to lock or unlock the door
    # First, put the gripper near the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper near the dial")
    # Once the gripper is near the dial, put the gripper on the dial.
    if check("the robot's gripper is near the dial"):
        robot.grab("the dial")
    # Once the gripper is on the dial, turn the dial to lock/unlock the door.
    if check("the robot's gripper is on the dial"):
        robot.turn("dial to lock or unlock door")
``