# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Put gripper roughly above target location
    #  2. Adjust gripper until it is above the target location
    # We want to move the robot's gripper above the target location.
    if check("the robot's gripper is not almost vertically aligned with the target location"):
        robot.move_gripper("almost vertically aligned with the target location")
    # Once we're above the target location, we can adjust until the gripper is
    # exactly above it.
    if check("the robot's gripper is not vertically aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location")