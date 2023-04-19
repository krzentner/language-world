if check("the robot's gripper is not above the peg in the hole"):
        robot.move("gripper above peg in hole")
    if check("the robot's gripper is not around the peg in the hole and the robot's gripper is open"):
        robot.drop("gripper around peg in hole")
    if check("the robot's gripper is near peg in hole and the robot's gripper is open"):
        robot.close("gripper around peg in hole")
    if check("the robot's gripper is above peg in hole and the robot's gripper is closed"):
        robot.move("peg to target location")