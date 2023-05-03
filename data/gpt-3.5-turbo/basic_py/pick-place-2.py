if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.grab("puck")
    if check("the robot's gripper is around the puck and the robot's gripper is not vertically aligned with target location"):
        robot.move("gripper above target location")
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.put("puck at target location")