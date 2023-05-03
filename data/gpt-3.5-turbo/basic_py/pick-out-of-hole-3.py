if check("the robot's gripper is not vertically aligned with the peg and the peg is in the hole"):
        robot.put("gripper above hole")
    if check("the robot's gripper is almost vertically aligned with the peg and the peg is inside the gripper"):
        robot.lift("the peg out of the hole")
    if check("the robot's gripper is not above the goal and the peg is outside the gripper"):
        robot.put("gripper above goal")
    if check("the robot's gripper is almost vertically aligned with the goal and the peg is inside the gripper"):
        robot.drop("the peg onto the goal")