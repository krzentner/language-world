if check("the robot's gripper is not above the peg in the hole"):
        robot.move("gripper to above peg in the hole")
    if check("the robot's gripper is not vertically aligned with the peg and the robot's gripper is not around the peg"):
        robot.put("gripper above the peg")
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around the peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around the peg")
    if check("the robot's gripper is above the hole and the robot's gripper is closed"):
        robot.lift("peg out of hole and hold it at target location")