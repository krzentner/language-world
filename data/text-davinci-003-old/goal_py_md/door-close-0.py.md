

Steps:
1. Put gripper left of the door handle
2. Push the door closed

    if check("the robot's gripper is not left of the door handle"):
        robot.move_gripper("left of the door handle")
    if check("the robot's gripper is left of the door handle"):
        robot.move_gripper("near the door handle")