
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed, but the wall blocks the path to goal"):
        robot.find("best path around wall")
    if check("the robot's gripper is vertically aligned with puck and the puck is below the robot's gripper"):
        robot.place("puck at goal")