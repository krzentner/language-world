
    if check(" the robot's gripper is not vertically aligned with the knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with the knob and the robot's gripper is not around the knob"):
        robot.put("gripper around knob")
    if check("the robot's gripper is around knob"):
        robot.turn("clockwise")