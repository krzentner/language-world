
    if check("the robot's gripper is not vertically aligned with the door lock knob"):
        robot.put("gripper up from door lock knob")
    if check("the robot's gripper is not around the door lock knob"):
        robot.drop('gripper around knob')
    if check("the robot's gripper is near the door lock knob"):
        robot.turnADegree("fifty degrees")