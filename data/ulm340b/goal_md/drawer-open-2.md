
    Choose your answer:
        o Open the drawer with gripper
        o Move the gripper left
        o Put gripper above the drawer handle / Drop gripper around drawer handle / Pull open the drawer
    First, put the gripper mostly above the drawer handle.
    - When the robot's gripper is not almost vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is closed
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is left of the drawer handle

The task `button-press` requires the robot to push the button down.
To push the button down reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper  2. Push down on the button
    To line the gripper up, we can either just put it next to the button or try to line it up from above. We want to line it up from above, so check if the gripper is near the button from above.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, what steps the robot should perform?
    Choose your answer:
        o Close the gripper / Move the gripper to the target location
        o Put gripper above the peg / Grab the peg with the gripper / Line the peg up with the hole / Insert the peg into the hole from above
        o Put gripper below the hole / Insert the peg into the hole from above
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg.
    - When the peg is not left