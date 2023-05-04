
Steps:  1. Put gripper above the lever  2. Drop gripper around lever  3. Pull the lever up
    The lever is a round object, so we need to align the robot's gripper around it before grabbing it.
    - When the robot's gripper is not vertically aligned with lever, the robot should put gripper above lever.
    If the robot's gripper is vertically aligned with the lever but not around it, it should move down to grab the lever.
    - When the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever, the robot should drop gripper around lever.
    If the gripper is around the lever, we can pull up on the lever to raise it.
    - When the robot's gripper is around lever, the robot should pull lever up.
"""


INSTRUCTIONS = """
The instructions we give are shown below. We'll let you practice each one and ask you about how the instructions work.

The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.


The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
Steps:  1. Put gripper left of the window handle  2. Start pushing against