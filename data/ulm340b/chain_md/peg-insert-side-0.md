
    Steps:  1. Put the gripper above the peg  2. Put the gripper around the peg  3. Close the gripper around the peg  4. Line up the peg with the hole  5. Put the peg into the hole
    In order to grab the peg, first we need to put the gripper roughly above the peg, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the peg and the robot's gripper is not around peg, the robot should place gripper above peg.
    Now that the gripper is above the peg, we can start moving it around the peg.
    - When the robot's gripper is above peg and the robot's gripper is not around peg, the robot should drop gripper around peg.
    If the gripper is near the peg and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near peg and the robot's gripper is open, the robot should close gripper around peg.
    In order to insert the peg from the side into the hole, we should first line up the peg with the hole
    - When the robot's gripper is around peg and the robot's gripper is closed, the robot should line up peg with hole.
    If the peg is above the hole as seen from the side, just drop the peg to put it into the hole.
    - When the peg is above hole and the peg is sideways in hole, the robot should place peg in hole.

The task `peg-unstack` requires the robot to lift the small cube off of the large cube, then move the small cube to the target location.
To lift the small cube off of the large cube reliably, what steps the robot should perform?
    Steps:  1. Grab the small cube  2. Move the small cube above the large cube
    Grab the small cube just like with `pick-place`.
    - When the robot's gripper is not above cube and the robot's gripper is not around cube, the robot should place gripper above cube.
    - When the robot's gripper is above cube and the robot's gripper is not around cube, the robot should drop gripper around cube.
    - When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
    If we're grabbing the small cube, lift it above the large cube.
    - When the robot's gripper is around cube and the robot's gripper is closed, the robot