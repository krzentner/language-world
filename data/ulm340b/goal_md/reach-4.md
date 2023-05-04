
    The task `reach` doesn't involve any special steps, because all the robot has to do is to reach the target location.
    Steps:  1. Reach to the target location

The task `peg-insert-front` requires the robot to grab the peg and insert it into the hole from the front.
To grab the peg and insert it into the hole from the front reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not forward aligned with the peg, move the robot's gripper until the robot's gripper is forward aligned with the peg
    Once the robot's gripper is forward aligned with the peg, move the gripper down around the peg.
    - When the robot's gripper is forward aligned with the peg, move the robot's gripper until the robot's gripper is above the peg
    As long as the gripper is around the peg, move the gripper around with the peg lined up with the hole.
    - When the robot's gripper is above the peg and the peg is horizontally aligned with the hole, move the robot's gripper until the robot's gripper is forward aligned with the peg
    If the peg is now aligned with the hole and in front of the gripper, we can push the peg into the hole.
    - When the robot's gripper is above the peg, move the robot's gripper until the robot's gripper is horizontally aligned with the hole

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper in the right direction  2. Push down on the button from the top
    If the robot's gripper is not lined up with the button to press it, line up the gripper.
    - When the robot's gripper is not vertically aligned with button and the robot's gripper is not left of the button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is not left of the button and the robot's gripper is left of button, move the