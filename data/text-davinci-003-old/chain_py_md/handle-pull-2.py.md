

The program should be:
```
# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up the handle
    # First, put the gripper almost above the handle, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, maybe we can pull it up by
    # closing the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # We closed the gripper, and the handle is still near the gripper, so maybe we
    # grabbed it.
    # Try to pull the handle up.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around handle and the robot's gripper is closed"):
        robot.pull("handle up")
```