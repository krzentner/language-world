
    if check("the robot's gripper is not near the door knob"):
        robot.reach("to door knob")
    if check("the robot's gripper is near the door knob"):
        robot.turn("knob clockwise")
    if check("the door knob is at the right position"):
        robot.pull("door open")