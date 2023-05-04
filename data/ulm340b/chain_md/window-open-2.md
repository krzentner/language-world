
    Steps:  1. Put gripper left of the window handle  2. Start pulling the window handle left to open the window

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Drop gripper down to the peg  3. Move gripper up with the peg  4. Insert the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put the gripper above the peg.
    If the gripper is still above the peg, close the gripper around the peg.
    - When the robot's gripper is above the peg and the robot's gripper is open, the robot should drop the gripper down to the peg.
    If the gripper is around the peg, move the gripper up to pick it up.
    - When the robot's gripper is around the peg and the peg is not vertically aligned with the robot's gripper, the robot should move gripper up with peg.
    If the peg is aligned with the robot's gripper and it's near the hole, push the peg down into the hole.
    - When the peg is vertically aligned with the robot's gripper and the peg is near the hole, the robot should insert peg into hole.



The following is the data we have collected from our study. Please let us know if there's anything wrong or we've missed something.

User info:
    Participant ID:
    Participant gender: male
    Participant native language:


    The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should reach to goal.

    The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to