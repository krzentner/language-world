

```
# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Line up the gripper with the mug handle
    #  2. Close gripper around the mug handle
    #  3. Pull the mug to the target location
    # First, line up the the gripper with the mug handle so it can grab it.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper is lined up, grab the mug handle by closing the gripper.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is open"):
        robot.grab("mug handle")
    # If the gripper is closed around the mug handle, pull the mug to the target
    # location.
    if check("the robot's gripper is closed around the mug handle"):
        robot.pull("mug to goal")
``