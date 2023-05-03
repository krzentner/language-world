To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly above the puck  2. Drop gripper around the puck  3. Push the puck towards the target
    First, put the gripper roughly above the puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above the puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around the puck and the robot's gripper is open, the robot should drop gripper around the puck.
    Once the gripper is around the puck, we can try to push it towards the goal. We should keep pushing until the puck has reached the goal location.
    - When the puck is not at the goal location, the robot should push the puck towards the target.