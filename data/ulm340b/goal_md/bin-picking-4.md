
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move cube into bin
    First, put the gripper roughly above cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above the cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is in the target bin and the robot's gripper is open

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not above the peg, move the robot's gripper until the robot's gripper is above the peg
    If the peg is not forward aligned with the robot's gripper, move the gripper down until it's around the peg.
    - When the peg is not forward aligned with the robot's gripper and the peg is above the robot's gripper, move the robot's gripper until the robot's gripper is around the peg and the robot's gripper is closed
    If the robot's gripper is not around the peg, put it around the peg.
    - When the robot's gripper is not around the peg and the robot's gripper is not closed, move the robot's gripper until the robot's gripper is around the peg and the robot's gripper is closed
    If the peg is not horizontally aligned with the hole, line it up.
    - When the peg is not horizontally aligned with the hole and the peg is horizontally aligned with the robot