

    [Answer: 2]
    [Answer: 1]
    [Answer: 2]
    [Answer: 4]
    [Answer: 1]

The task `knob-turn-left` requires the robot to grab the knob and rotate it counter-clockwise.
To grab the knob and rotate it counter-clockwise reliably, what steps the robot should perform?

    [Answer: 1]
    [Answer: 2]
    [Answer: 1]
    [Answer: 3]
    [Answer: 3]

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the button, the robot should put the gripper above the button.
    - When the robot's gripper is above the button, the robot should put the gripper to the left of the button.
    - When the robot's gripper is left of the button and the robot's gripper is not in front of the button, the robot should slide gripper towards button.
    - When the robot's gripper is in front of button, the robot should push on button.

The task `knob-turn-right` requires the robot to grab the knob and rotate it clockwise.
To grab the knob and rotate it clockwise reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the knob, the robot should place the gripper above the knob.
    - When the robot's gripper is not around the knob, the robot should drop the gripper around the knob.
    - When the robot's gripper is around the knob and not in front of the knob, the robot should push the gripper forward.
    - When the robot's gripper is near the knob and in front of the knob, the robot should turn the knob clockwise.

The task `push-back` requires the robot to push the drawer back closed.
To push the drawer back closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the drawer handle, the robot should move the gripper above the drawer handle.
    - When the robot's gripper is not in front of the drawer handle, the robot should move the gripper in front of the drawer handle.
    - When the robot's gripper is around the drawer handle, the robot should slide the drawer closed.
""".strip().replace('\n', ' ')


def main():
    # Define the list of all