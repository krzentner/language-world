if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is holding the puck and the robot's hand is not at the target location"):
        robot.move("hand to target location")
    if check("the robot's hand is at the target location and the robot's gripper is holding the puck"):
        robot.drop("puck at target location")