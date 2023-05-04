
Steps:

The task `peg-insert-topdown` requires the robot to drop the peg into the hole from the top.
To drop the peg into the hole from the top reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above hole  2. Put peg in gripper above hole  3. Drop the peg into the hole
    The robot needs to start by getting the gripper above the hole.
    - When the robot's gripper is not above the hole, the robot should put gripper above hole.
    If the peg is still in the gripper, then it's not aligned above the hole, so we need to align it.
    - When the peg is in the gripper and the robot's gripper is not vertically aligned with the hole, the robot should align peg and hole.
    Finally, if the peg is in the robot's gripper above the hole, drop it in.
    - When peg is in the gripper and the robot's gripper is vertically aligned with the hole, the robot should drop peg into hole.

The task `pick` requires the robot to pick up the puck.
To pick up the puck reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.

The task `reach-push` requires the robot to push an object at the target location.
To push an object at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper around object  2. Push object to the target location
    First, put the gripper around the object
    - When the robot's gripper is not around the object and the robot's gripper is open, the robot should put gripper around object.
    Once the gripper is around the object,