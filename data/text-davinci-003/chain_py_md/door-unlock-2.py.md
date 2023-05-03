

The robot should:

1. Put gripper above door dial
2. Place gripper around door dial
3. Turn the dial clockwise

if check("the robot's gripper is not above the door dial"):
    robot.place("gripper above door dial")
if check("the robot's gripper is not around the door dial and the robot's gripper is open"):
    robot.put("gripper around door dial")
if check("the robot's gripper is around the door dial"):
    robot.turn("dial clockwise")