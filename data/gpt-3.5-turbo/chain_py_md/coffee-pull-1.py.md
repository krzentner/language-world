# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper around mug handle
    #  2. Pull the mug to the target location
    # First, line up the gripper so that it's around the handle of the mug.
    if check("the robot's gripper is not around the mug handle"):
        robot.grab("mug handle")
    # Once the gripper is around the handle of the mug, pull the mug to the target
    # location.
    if check("the robot's gripper is around mug handle"):
        robot.pull("mug to target location")