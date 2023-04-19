
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around the puck and the gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is around the puck and the gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around the puck and the gripper is closed"):
        robot.place("puck at target")