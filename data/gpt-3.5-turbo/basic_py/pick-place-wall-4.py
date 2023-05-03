if check("the robot's gripper is not above the puck and the robot's gripper is not above the wall"):
        robot.put("gripper above the puck and the wall")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("gripper above wall")
        robot.place("puck at goal on top of the wall")