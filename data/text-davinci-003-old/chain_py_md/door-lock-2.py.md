

The steps are as follows:

1. Put gripper above the door handle
2. Drop gripper around the door handle
3. Turn the dial on the door

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Turn the dial on the door
    # First, put the gripper roughly above the door handle, so that we don't
    # bump it while trying to grab it.
    if check("the robot's gripper is not above the door handle"):
        robot.place("gripper above door handle")
    # If the gripper isn't around the door handle, put it around the door handle.
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.drop("gripper around door handle")
    # If the gripper is near the door handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near door handle and the robot's gripper is open"):
        robot.close("gripper around door handle")
    # We closed the gripper, and the door handle is still near the gripper, so
    # maybe we grabbed it.
    # Try to turn the dial on the door.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above door handle and the robot's gripper is closed"):
        robot.turn("dial clockwise")
```