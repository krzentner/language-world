
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.put("the gripper around the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.grab("the puck")
    if check("the puck is in the robot's gripper and the destination is not to the left of the robot's gripper"):
        robot.move("puck to goal")