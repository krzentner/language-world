
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is near the peg and the peg is still inside the hole"):
        robot.pull("peg from hole")
    if check("the robot's gripper is near the peg and the peg is no longer inside the hole"):
        robot.close("gripper around peg")