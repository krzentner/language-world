
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, move the robot's gripper until the robot's gripper is around the door handle

The task `button-press-side` requires the robot to press the button by pushing the button from the side.
To press the button by pushing the button from the side reliably, what steps the robot should perform?
    Steps:  1. Line up the gripper from the side  2. Push the button from the side
    The button is on the table and doesn't have a handle, so we can press it directly using the front face of the robot's gripper.
    - When the robot's gripper is forward aligned with button, move the robot's gripper until the robot's gripper is not forward aligned with button
    As long as we are pushing the button from the side, we can just keep pushing it in that direction.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is forward aligned with button

The task `door-unlock` requires the robot to grab the peg and insert it into the door to unlock it.
To grab the peg and insert it into the door to unlock it reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the door  4. Insert the peg into the door
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned