

if check("the robot's gripper is not above the hole"):
        robot.place("gripper above hole")
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.lift("peg out of hole")
    if check("the robot's gripper is not near the goal"):
        robot.place("peg at goal")