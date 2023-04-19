
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is around wrench and the wrench is not above peg"):
        robot.put("wrench above peg")
    if check("the robot's gripper is around wrench and the wrench is above peg"):
        robot.place("wrench around peg")