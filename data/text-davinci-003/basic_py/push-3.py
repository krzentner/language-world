
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is near the puck and the puck is not aligned to reach target"):
        robot.align("puck to reach target")
    if check("the robot's gripper is above the puck and the puck is aligned to reach target"):
        robot.slide("puck to target")
        robot.release("puck")