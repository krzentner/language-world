if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the puck is not touching the wall"):
        robot.push("the gripper into the puck and towards the wall")
    if check("the puck is touching the wall and the robot's gripper is near the puck"):
        robot.slide("the puck to the goal while pushing against the wall")