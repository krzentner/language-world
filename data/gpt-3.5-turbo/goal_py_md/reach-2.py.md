# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Put gripper near target location
    #  2. Check if the gripper is close enough to the target location
    #  3. If not, move the gripper closer until it is
    # First, put the gripper roughly near the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Check if the gripper is close enough to the target location.
    if check("the robot's gripper is not within 1 inch of the target location"):
        robot.move_gripper("closer to the target location")