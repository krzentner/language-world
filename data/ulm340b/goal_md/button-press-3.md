

The task `peg-unstack` requires the robot to unstack the blue peg from the red one.
To unstack the blue peg from the red one reliably, what steps the robot should perform?

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near the button  2. Push the button from the side
    We want to push the button on the side so we need to put the gripper near the button and align it from the side.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button
    If the gripper is almost vertically aligned with the button, close the gripper.
    - When the robot's gripper is forward aligned with button, move the robot's gripper until the robot's gripper is near the button and the robot's gripper is closed
    If the gripper is near the button and is closed, we can push the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is forward aligned with button

The task `peg-insert-front` requires the robot to grab the peg and insert it into the hole from the front.
To grab the peg and insert it into the hole from the front reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper above the peg  2. Drop the gripper around the peg  3. Line up the peg with the hole from the front  4. Insert the peg
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    Once the gripper is lined up above the peg, we should be able to grab the peg by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the peg, move the robot's gripper until the robot's gripper is around the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole from the front.
    - When peg is horizontally aligned with hole and the robot's gripper is around the peg, move the robot'