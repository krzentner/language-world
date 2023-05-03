
    if check("there is a wall in between the robot's gripper and the puck"):
        robot.align("wall with puck")
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.close("gripper around puck")
    if check("the robot's gripper is closed"):
        robot.place("puck at goal")