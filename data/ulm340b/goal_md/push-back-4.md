
"""

# Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


print("""The task `push-back` requires the robot to slide the puck backwards to the target location.
To slide the puck backwards to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper backwards into top of puck  3. Slide puck to goal
    The robot can slide the puck backwards by trapping it by pushing backwards into it from above and moving the gripper. If the puck isn't behind the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not backwards aligned with the puck, move the robot's gripper until the robot's gripper is backwards aligned with the puck
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is backwards aligned with the puck and the robot's gripper is not above puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper until the robot's gripper is near the target location
""")

# Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

print("""The task `drawer-close-side` requires the robot to push the drawer closed from the side.
To push the drawer closed from the side reliably, what steps the robot should perform?
""")

# Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

print("""The task `drawer-open-side` requires the robot to pull the drawer open from the side.
To pull the drawer open from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    We need to put the gripper above the drawer handle before we can grab it,