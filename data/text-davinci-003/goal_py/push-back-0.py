
    # Steps:
    #  1. Put gripper behind puck
    #  2. Push gripper into back of puck
    #  3. Slide puck to goal
    # As with the forward push, the robot can slide the puck by trapping it
    # between the gripper and some surface.
    if check("the robot's gripper is not behind puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")

    if check("the robot's gripper is behind the puck and the robot's gripper is near the puck"):
        robot.move_gripper("above the target location")

    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not near puck"):
        robot.move_gripper("behind the puck", close_gripper=True)