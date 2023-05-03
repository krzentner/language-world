
    if check("the robot's gripper is not above the peg in the hole"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg in the hole and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is not below the peg in the hole and the robot's gripper is closed"):
        robot.place("gripper below peg")
    if check("the robot's gripper is below the peg in the hole and the robot's gripper is closed"):
        robot.pull("peg out of hole")
    if check("the robot's gripper is above the peg in the hole and the robot's gripper is closed"):
        robot.place("peg at goal")