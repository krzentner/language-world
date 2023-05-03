The task `dial-turn` requires the robot to turn the dial.
To turn the dial reliably, the robot should perform the following steps:
    Steps:  1. Put gripper around the dial handle  2. Turn the dial to the desired position
    First, move the gripper around the dial handle, so that we have a firm grip on it.
    - When the robot's gripper is not around the dial handle, the robot should put gripper around the dial handle.
    Once the gripper is around the dial handle, we can turn the dial to the desired position. We can use incremental turning done in a loop to turn the dial at a specific angle.
    - When the robot's gripper is around the dial handle, the robot should turn the dial to the desired position.