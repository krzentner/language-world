if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.grab("puck")
    if check("the robot's gripper is around the puck and the robot is not vertically aligned with the target location"):
        robot.move("gripper to the target location")
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.release("puck at the target location")