# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above handle of the mug
    #  2. Drop gripper around mug handle
    #  3. Close gripper around handle
    #  4. Move mug to target location
    # First, put the gripper above the handle of the mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the mug handle"):
        robot.put("gripper above mug handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.drop("gripper around mug handle")
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the mug to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above mug handle and the robot's gripper is closed"):
        robot.pull("mug to target location")