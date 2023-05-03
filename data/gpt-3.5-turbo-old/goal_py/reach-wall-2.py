# Steps:
    #  1. Move gripper over the wall
    #  2. Move gripper down to target location
    # In this case, we need to move the gripper over the wall first before
    # moving it down to the target location.
    if check("the robot's gripper is not over the wall and the robot's gripper is not vertically aligned with the target location"):
        robot.move_gripper("over the wall")
    # Once the gripper is over the wall, move it down to the target location.
    if check("the robot's gripper is over the wall and the robot's gripper is not vertically aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location")