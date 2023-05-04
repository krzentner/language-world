
Steps:

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the side  2. Push down on the button from the side
    Because this is "side", we just need to line up the gripper from the side. Line up the robot's gripper from the side.
    - When the robot's gripper is not horizontally aligned with button, move the robot's gripper until the robot's gripper is horizontally aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is horizontally aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, move the robot's gripper until the robot's gripper is around the door handle

The task `knob-turn-left` requires the robot to rotate the knob counter-clockwise until it stops.
To rotate the knob counter-clockwise until it stops reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the knob  2. Drop gripper around the knob  3. Rotate the knob counter-clockwise
    First, put the gripper roughly above the knob.
    - When the robot's gripper is not vertically aligned with knob, move the robot's gripper until the robot's gripper is vertically aligned with the knob
    If the gripper is above the knob we should be able to grab it.
    - When the robot's gripper is vertically aligned with knob, move the robot's gripper until the robot's gripper