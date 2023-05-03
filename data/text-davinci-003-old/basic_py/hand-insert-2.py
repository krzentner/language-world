
    if check("the robot's gripper is not above the puck and the robot's gripper is open"):
        robot.put("gripper above puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around the puck and the robot's gripper is closed"):
        robot.lift("puck from initial location")
    if check("the robot's gripper is near the target location and the puck is in the robot's gripper"):
        robot.place("puck at target")