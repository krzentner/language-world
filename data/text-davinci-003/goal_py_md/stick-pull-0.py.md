

# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put gripper near the stick 
    #  2. Align the gripper with the stick
    #  3. Grip the end of the stick
    #  4. Move the stick to pull the thermos to the target location
    # To begin, move the gripper near the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick")
    # Next, we want to align the gripper with the stick, so that the robot can
    # grip the stick.
    if check("the robot's gripper is near the stick and the robot's gripper is not horizontally aligned with the stick"):
        robot.move_gripper("horizontally aligned with the stick", close_gripper=True)
    # Once the gripper is aligned with the stick, we can grip the end of the
    # stick with the robot's gripper.
    if check("the robot's gripper is horizontally aligned with the stick"):
        robot.move_gripper("near the stick and around the stick")
    # Now that the robot has control of the stick, move the stick to pull the
    # thermos to the target location.
    if check("thermos is not near the target location and the robot's gripper is around the stick"):
        robot.move_gripper("near the target location")