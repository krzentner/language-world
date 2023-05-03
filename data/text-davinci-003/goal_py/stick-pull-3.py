
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Pull thermos to goal by moving stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Once the gripper is around the stick and closed, we can start pulling the
    # thermos with it.
    if check("the robot's gripper is near the stick and the robot's gripper is closed"):
        robot.move_gripper("near the target location")