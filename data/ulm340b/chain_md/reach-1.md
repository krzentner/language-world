:
    Steps:  1. Put gripper at goal

The task `knob-turn-cw` requires the robot to rotate the knob clockwise.
To rotate the knob clockwise reliably, the robot should perform the following steps:
    Steps:  1. Put gripper below the knob  2. Close gripper around knob  3. Twist gripper to turn the knob
    Start by placing the gripper below the knob as seen from in front of the robot.
    - When the robot's gripper is not vertically aligned with knob and the robot's gripper is below knob, the robot should put the gripper below the knob.
    If the gripper is in front of the knob but not closed, close it.
    - When the robot's gripper is forward aligned with the knob and the robot's gripper is open, the robot should close gripper around knob.
    If the gripper is mostly aligned with the knob, we can just turn it.
    - When the robot's gripper is forward aligned with knob, the robot should rotate gripper cw.

The task `knob-turn-ccw` requires the robot to rotate the knob counter-clockwise.
To rotate the knob counter-clockwise reliably, the robot should perform the following steps:
    Steps:  1. Put gripper below the knob  2. Close gripper around knob  3. Twist gripper to turn the knob
    Start by placing the gripper below the knob as seen from in front of the robot.
    - When the robot's gripper is not vertically aligned with knob and the robot's gripper is below knob, the robot should put the gripper below the knob.
    If the gripper is in front of the knob but not closed, close it.
    - When the robot's gripper is forward aligned with the knob and the robot's gripper is open, the robot should close gripper around knob.
    If the gripper is mostly aligned with the knob, we can just turn it.
    - When the robot's gripper is forward aligned with knob, the robot should rotate gripper ccw.

The task `peg-unstack` requires the robot to lift the peg out of the hole by gripping it.
To lift the peg out of the hole by gripping it reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Put the gripper around the peg  3. Lift the gripper to take the peg out of the hole
    Start by placing the gripper below the peg as seen from in front of the robot.
    - When the robot's gripper is not above