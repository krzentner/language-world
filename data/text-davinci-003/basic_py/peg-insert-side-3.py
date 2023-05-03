
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.move("towards the gap between peg and target")
    if check("the robot's gripper is inside the target"):
        robot.place("peg into target")