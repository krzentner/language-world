# door-open: pull the door open
def door_open(robot):
    # Steps:
    # 1. Line up the gripper with the door handle
    # 2. Grab the door handle
    # 3. Pull the door open
    # First, put the gripper above the door handle
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Next, grab the door handle
    if check("the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Finally, pull the door open
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")