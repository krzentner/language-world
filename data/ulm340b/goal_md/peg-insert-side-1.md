
    Steps:  1. Drop gripper around peg  2. Lift peg up above target  3. Slide peg into target
    First, put the gripper around the peg.
    - When the robot's gripper is not around peg and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the peg and the robot's gripper is closed
    If the gripper is near the peg, it might be closed around the peg. If the peg is above the target, then we can slide the peg into the target.
    - When the robot's gripper is near the peg, move the robot's gripper until the robot's gripper is above the target
    If the peg is not aligned with the target yet, move the peg along the edge to slide it into the target.
    - When the robot's gripper is vertically aligned with the target location, move the robot's gripper until the robot's gripper is near the target location and the peg is above the target location

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, what steps the robot should perform?
    Steps:  1. Move gripper above peg  2. Close gripper around peg  3. Lift peg up above target  4. Drop peg into target
    First, put the gripper above the peg.
    - When the robot's gripper is not above peg and the robot's gripper is open, move the robot's gripper until the robot's gripper is above the peg and the robot's gripper is closed
    If the gripper is above the peg, we might be able to close it around the peg. If the peg is above the target, then we can drop the peg into the target.
    - When the robot's gripper is above the peg, move the robot's gripper until the robot's gripper is above the target
    If the peg is not aligned with the target yet, move the peg down to slide it into the target.
    - When the robot's gripper is near the peg, move the robot's gripper until the robot's gripper is near the target location

The task `pull-drawer` requires the robot to open the drawer by pulling the drawer handle.
To open the drawer by pulling the drawer handle reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open