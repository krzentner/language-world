
    if check("the robot's gripper is far from the mug"):
        robot.navigate("to the mug")
    if check("the robot's gripper is near the mug and the robot's gripper is not around the mug's handle"):
        robot.grab("mug's handle")
    if check("the robot's gripper is around the mug's handle"):
        robot.pull("mug to goal")