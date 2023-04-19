
    if check("the robot's gripper is not above the mug"):
        robot.reach("above mug")
    if check("the robot's gripper is above the mug and the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is around mug"):
        robot.move("mug to goal")