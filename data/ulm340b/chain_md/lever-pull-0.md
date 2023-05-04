
    Steps:  1. Put the gripper above the left side of the lever  2. Push down on the left side of the lever  3. Rotate the lever
    The robot can push the lever up by pushing down on the left side of the lever. If the lever isn't below the gripper as seen from above, move the gripper above the lever.
    - When the robot's gripper is not above the left side of the lever and the robot's gripper is not vertically aligned with the left side of the lever, the robot should put the gripper above the left side of the lever.
    If the gripper is aligned with the lever but not near it, move the gripper down to the lever to rotate it.
    - When the robot's gripper is vertically aligned with the left side of the lever and the robot's gripper is not near the left side of the lever, the robot should push the gripper down on the left side of the lever.
    If the gripper is near the lever, we've probably trapped the lever and can rotate it.
    - When the robot's gripper is near the left side of the lever, the robot should rotate the lever.

The task `peg-unstack` requires the robot to lift the top peg off of the bottom peg.
To lift the top peg off of the bottom peg reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper above the top peg  2. Grab the top peg  3. Lift the top peg
    First, put the gripper roughly above the top peg, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the top peg, the robot should put the gripper above the top peg.
    If the gripper isn't around the top peg, put it around the top peg.
    - When the robot's gripper is not around the top peg and the robot's gripper is open, the robot should put the gripper around the top peg.
    If the gripper is near the top peg and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near the top peg and the robot's gripper is open, the robot should close the gripper around the top peg.
    We closed the gripper, and the top peg is still near the gripper, so maybe we grabbed it. Try to lift it. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is around the top peg and