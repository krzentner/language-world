if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around the peg and the wrench"):
        robot.twist("wrench around peg")