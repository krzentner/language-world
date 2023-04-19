

1. Put gripper as viewed from above the handle
2. Push down on the handle

if check("the robot's gripper is not vertically aligned with handle"):
    robot.move_gripper("vertically aligned with the handle", close_gripper=True)

if check("the robot's gripper is vertically aligned with handle"):
    robot.move_gripper("downward alignment with the handle")