
    # Steps:
    #  1. Put gripper near the goal
    #  2. Push gripper into the goal
    #  3. Move gripper to target location
    # First, move the gripper to a position near the goal.
    if check("the robot's gripper is not near the goal"):
        robot.move_gripper("near the goal")
    # Then, push the gripper into the goal towards the target location.
    if check("the robot's gripper is not moving"):
        robot.move_gripper("above the goal", close_gripper=True)
    # Finally, move the gripper to the target location.
    if check("the robot's gripper is not moving"):
        robot.move_gripper("above the target location")