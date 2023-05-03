
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the peg is not horizontally aligned with the robot's gripper and the robot's gripper is open"):
        robot.align("gripper with the peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is near the peg and the robot's gripper is closed"):
        robot.move("puck to goal")