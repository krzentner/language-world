
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.put("gripper above window handle")
    if check("the robot's gripper is vertically aligned with window handle and the window handle is right of the robot's gripper and the robot's gripper is open"):
        robot.grab("window handle")
    if check("the robot's gripper is around window handle and the window handle is on the left of the robot's gripper"):
        robot.slide("window left")