
    if check("the robot's gripper is not vertically aligned with the knob on the door"):
        robot.put("gripper near knob")
    if check("the robot's gripper is around the button and the robot's gripper is open"):
        robot.put("gripper around knob")
    if check("the robot's gripper is around the knob and the knob is not locked"):
        robot.turn("knob clockwise")
    if check("the knob is locked"):
        robot.stop("turning knob")