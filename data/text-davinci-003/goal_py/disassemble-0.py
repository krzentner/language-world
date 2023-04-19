
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Reach around the wrench
    #  3. Pull the wrench off the peg
    # This task involves two objects, so there are two steps here.
    # First, we need to reach around the wrench with the gripper
    if check("the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench")
    # Once the gripper is around the wrench, we can pull on it and the wrench
    # will come off the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("away from the peg")