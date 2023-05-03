# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug's handle
    #  2. Grab the mug with the gripper
    #  3. Line the mug's handle up with the target location
    #  4. Pull the mug towards the target location
    # First, put the gripper above the mug's handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is lined up above the mug handle, we should be able to
    # grab it by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.put("gripper around mug handle")
    # Once the gripper is around the mug handle, we need to line up the handle
    # with the target location.
    if check("the robot's gripper is around mug handle and the mug handle is not aligned with target location"):
        robot.align("mug handle to target location")
    # If the mug handle is aligned with the target location to the side, we can
    # pull it towards the target location.
    if check("the mug handle is horizontally aligned with target location"):
        robot.pull("mug towards target location")