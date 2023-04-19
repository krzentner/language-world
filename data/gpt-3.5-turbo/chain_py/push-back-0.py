# Steps:
    #  1. Put gripper above the puck
    #  2. Push gripper into the top of the puck
    #  3. Slide the puck backward to the goal
    # This is almost the same as the push function, except we need to move the
    # puck backward instead of forward.
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it backward to the goal.
    # We need to use a different function to slide it backward.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide_back("the puck to the goal")