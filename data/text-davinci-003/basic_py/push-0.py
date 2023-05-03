
    if check("the robot's gripper is above the puck"):
        robot.put("gripper around puck")
    if check("the puck is not horizontally aligned with the target location"):
        robot.align("puck to goal")
    if check("the puck is horizontally aligned with the target location and the robot's gripper is almost vertically aligned with the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.slide("puck to goal")