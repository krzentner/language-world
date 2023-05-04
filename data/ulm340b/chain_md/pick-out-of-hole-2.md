
    Steps:  1. Place gripper above the peg  2. Drop the gripper around the peg  3. Pull the peg out of the hole
    First, put the gripper roughly above the peg, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the peg, the robot should place gripper above peg.
    If the gripper isn't around the peg, drop it around the peg.
    - When the robot's gripper is not around peg and the robot's gripper is open, the robot should drop gripper around peg.
    If the gripper is around the peg, we can pull it out by moving the gripper up.
    - When the robot's gripper is around peg, the robot should pull peg out of hole.

The task `pick-place-with-clutter` requires the robot to pick up the puck among clutter and hold it at the target location.
To pick up the puck among clutter and hold it at the target location reliably, what steps the robot should perform?
    Steps:  1. Place gripper above the puck  2. Move the gripper away from clutter  3. Drop the gripper around the puck  4. Move the gripper away from clutter  5. Close the gripper around the puck  6. Move the puck to the target location
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper is near other objects, move it away to avoid grasping one of them.
    - When the robot's gripper is near clutter, the robot should move gripper away from clutter.
    If the gripper is roughly lined up around the puck, drop the gripper around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near other objects, move it away to avoid grasping one of them.
    - When the robot's gripper is near clutter, the robot should move gripper away from clutter.
    If the gripper is near the puck and open, close the gripper to grab the puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    If the gripper is lined up with the puck, we might have the puck, so let'