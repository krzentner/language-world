
    if check("the robot's gripper is not almost vertically aligned with the peg"):
        robot.move("gripper to above peg")
    if check("the robot's gripper is almost vertically aligned with peg and the robot's gripper is not above peg"):
        robot.put("gripper above peg")
    if check("robot's gripper is above peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.place("peg at goal")