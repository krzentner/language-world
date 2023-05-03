
    # Steps:
    #  1. Put gripper left of puck
    #  2. Start pushing against the puck to move it
    #  3. Push the puck harder
    # First, put the gripper is not left of the puck, so we can start pushing.
    if check("puck right of the robot's gripper"):
        robot.move("gripper to left of puck")
    # If the robot's gripper is near the puck, we can probably slide the puck
    # now by pushing it to the left
    if check("the robot's gripper is near the puck"):
        robot.slide("puck left")
    # Keep pushing the puck to the left if it's still not at the goal
    if check("the puck is not at the goal"):
        robot.push("puck left harder")