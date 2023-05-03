# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move gripper above the target location
    #  2. Open the gripper
    # First, put the gripper above the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Open the gripper to release any object held by the gripper.
    if check("the robot's gripper is not open"):
        robot.move_gripper("above the target location", close_gripper=False)