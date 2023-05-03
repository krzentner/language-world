
    if check("the robot's gripper is not horizontally aligned with door lock"):
        robot.put("gripper near door lock")
    if check("the robot's gripper is horizontally aligned with door lock and the robot's gripper is open"):
        robot.close("gripper around door lock")
    if check("the robot's gripper is around door lock"):
        robot.turn("clockwise")
        robot.turn("counter-clockwise")