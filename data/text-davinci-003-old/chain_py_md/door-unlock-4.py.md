

Steps: 
1. Put gripper above doorknob
2. Position gripper around doorknob
3. Turn the dial clockwise

If the robot's gripper is not above the doorknob, move the gripper above it.
if check("the robot's gripper is not above the doorknob"):
    robot.put("gripper above doorknob")

Once the gripper is roughly above the doorknob, move it around so it can grip
the doorknob.
if check("the robot's gripper is not around the doorknob"):
    robot.drop("gripper around doorknob")

Once the gripper is around the doorknob, turn the dial clockwise.
if check("the robot's gripper is around the doorknob"):
    robot.turn("dial clockwise")