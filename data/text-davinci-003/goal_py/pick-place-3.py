
    # Steps:
    #  1. Put gripper above puck
    #  2. Pick up puck
    #  3. Place puck at target location
    # First, the robot must put its gripper above the puck to pick it up.
    # Because the robot is going to pick the puck up, the gripper must first be
    # lined up with the puck as seen from above.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Now, the gripper is lined up with the puck from above, so the robot can
    # pick it up by moving the gripper downward to grasp it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not holding the puck"):
        robot.move_gripper("below the puck", close_gripper=True)

        # Now that the puck is held, move the puck to the target location.
    if check("the robot's gripper is holding the puck"):
        robot.move_gripper("above the target location")