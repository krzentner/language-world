
    if check("the robot's gripper is not above wrench"):
        robot.place("gripper above wrench")
    if check("the wrench is not grabbed by the robot's gripper"):
        robot.grab("wrench")
    if check("the wrench is pulled away from the peg"):
        robot.pull("wrench off peg")