# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper around the mug handle
    #  2. Pull the mug towards the target location
    # First, align the gripper with the mug handle.
    if check("the robot's gripper is not near the mug handle"):
        robot.move_gripper("near the mug handle", close_gripper=True)
    # If the gripper is around the mug handle, pull the mug towards the target
    # location.
    if check("the robot's gripper is around the mug handle and not near the target location"):
        robot.move_gripper("near the target location")