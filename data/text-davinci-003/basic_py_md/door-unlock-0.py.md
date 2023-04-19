

If check("the robot's gripper is not vertically aligned with the door knob"):
    robot.put("gripper above door knob")
if check("the robot's gripper is vertically aligned with the door knob"):
    robot.grab("door knob")
if check("the robot's gripper is around the door knob"):
    robot.turn("dial in clockwise direction") 
if check("the dial is turned and pulled open"):
    robot.open("Door")