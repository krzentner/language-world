

The robot should reach to the target location by moving the gripper onto the location.

# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Put gripper above target location
    #  2. Move gripper onto target location
    # First, put the gripper above the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Now that the gripper is above the target location, move the gripper onto it.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("near the target location")