
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Lift the peg out of the hole  4. Hold the peg at the target location
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    As long the gripper is still mostly around the peg and the peg is not out of the hole, lift the peg out of the hole.
    - When the peg is in the hole, move the robot's gripper until the robot's gripper is above the peg
    If the peg is out of the hole, bring it to the target location.
    - When the robot's gripper is above the peg and the peg is out of the hole, move the robot's gripper until the robot's gripper is above the target location

The task `pick-out-of-hole-topdown` requires the robot to pick up the peg out of the hole from above and hold it at the target location.
To pick up the peg out of the hole from above and hold it at the target location reliably, what steps the robot should perform?
    Steps:  1. Line up the gripper as viewed from above  2. Close the gripper around the peg  3. Lift the peg out of the hole  4. Move the peg to the goal location
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with peg, move the robot's gripper until the robot's gripper is vertically aligned with peg
    If the gripper is aligned with the peg but not closed around it, drop the gripper around the peg.
    - When the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the peg, move the robot's gripper until the robot's gripper is closed and the robot's gripper is near the peg
    If the gripper is around the peg, lift the peg out of the hole.
    - When the peg is in the hole, move the robot's gripper until the robot's gripper is above the peg
    When the peg is out of the hole, move the peg to the goal location.
    - When the robot's gripper is vertically aligned with the peg and the peg is out of the hole, move the robot's gripper until the robot's