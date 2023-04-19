

Steps:
1. Put the gripper above the handle
2. Drop the gripper around the handle
3. Push down on the handle

```
# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push down on handle
    # First, put the gripper roughly above handle, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # We closed the gripper, and the handle is still near the gripper, so maybe
    # we grabbed it.
    # Try to push the handle down.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above handle and the robot's gripper is closed"):
        robot.push("down on handle")