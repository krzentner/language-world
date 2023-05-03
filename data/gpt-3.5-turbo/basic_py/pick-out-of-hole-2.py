if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the peg is not within the gripper and the gripper is open"):
        robot.move("gripper to hole")
        robot.grab("peg")
    if check("the peg is within the gripper and the gripper is closed"):
        robot.move("gripper to goal")
    if check("the gripper is above the goal and the peg is within the gripper"):
        robot.release("peg at goal")