if check("the robot's gripper is not vertically aligned with the peg in the hole"):
        robot.put("gripper above peg in hole")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg in the hole and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg in the hole and the robot's gripper is closed"):
        robot.move("gripper to target location")
    if check("the robot's gripper is at the target location"):
        robot.drop("gripper around peg")