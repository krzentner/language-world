

Steps:
1. Put gripper above door knob
2. Grab door knob
3. Turn the door knob

if check("the robot's gripper is not above door knob"):
  robot.put("gripper above door knob")

if check("the robot's gripper is above door knob and the robot's gripper is not around the door knob"):
 robot.grab("door knob")

if check("the robot's gripper is around door knob"):
 robot.turn("clockwise or counterclockwise")