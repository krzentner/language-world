# Steps:
    #  1. Put gripper above plate, gripper open
    #  2. Lower gripper onto plate and close gripper
    #  3. Slide plate sideways towards target location
    #  4. Release plate by opening gripper
    # First, put the gripper above the plate and open the gripper
    if check("the robot's gripper is not above the plate and the robot's gripper is not open"):
        robot.move_gripper("above the plate", close_gripper=False)
    # If the gripper is above the plate, lower it down until it grasps the plate
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("onto the plate", close_gripper=True)
    # Once the gripper is holding the plate, slide the plate sideways towards the target location
    if check("the robot's gripper is around the plate and the robot's gripper is not horizontally aligned with target location"):
        robot.move_gripper("horizontally aligned with target location")
    # Once the plate is at the target location, release the gripper to drop the plate
    if check("the robot's gripper is horizontally aligned with target location and the robot's gripper is closed"):
        robot.move_gripper("above the plate", close_gripper=False)