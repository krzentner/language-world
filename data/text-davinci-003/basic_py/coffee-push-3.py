
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.grab("mug")
    if check("the robot's gripper is below mug and the robot's gripper is open"):
        robot.grab("mug")
    if check("the robot's gripper is around the mug and the mug is not left of the robot's gripper"):
        robot.push("mug left")
    if check("the mug is left of the robot's gripper"):
        robot.place("mug at goal")