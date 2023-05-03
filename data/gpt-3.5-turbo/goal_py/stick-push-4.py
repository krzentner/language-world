# Steps:
    #  1. Put gripper above stick
    #  2. Grab the stick with the gripper
    #  3. Put gripper near the thermos
    #  4. Push thermos with the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper is above the stick, grab it with the gripper.
    if check("the robot's gripper is above the stick and the robot's gripper is not closed around the stick"):
        robot.move_gripper("around the stick")
    # Put the gripper near the thermos so that we can push it with the stick.
    if check("the robot's gripper is not near the thermos"):
        robot.move_gripper("near the thermos")
    # Push the thermos with the stick.
    if check("the robot's gripper is near the thermos and the stick is grabbed by the gripper"):
        robot.move_gripper("almost vertically aligned with the thermos")