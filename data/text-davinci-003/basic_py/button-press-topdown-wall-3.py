
    if check("the robot's gripper is not vertically aligned with button and the wall is in the way"):
        robot.put("gripper to the side of button")
    if check("the wall is blocking the robot's gripper"):
        robot. pushes("slide wall aside")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
    if check("the wall is blocking the button"):
        robot.push("slide wall aside")