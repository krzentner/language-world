
    Steps:  1. Put gripper above the faucet handle  2. Grab the faucet handle  3. Turn the faucet handle left
    First, put the gripper above the faucet handle.
    - When the robot's gripper is not vertically aligned with faucet handle, the robot should put gripper above faucet handle.
    When the gripper is above the handle, grab it.
    - When the robot's gripper is vertically aligned with faucet handle and the robot's gripper is open, the robot should close gripper around faucet handle.
    Since we grabbed the handle and want to turn it, just rotate the gripper to the left.
    - When the robot's gripper is around faucet handle, the robot should rotate the gripper left.

The task `faucet-close` requires the robot to turn the faucet right.
To turn the faucet right reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the faucet handle  2. Grab the faucet handle  3. Turn the faucet handle right
    Put the gripper above the faucet handle.
    - When the robot's gripper is not vertically aligned with faucet handle, the robot should put gripper above faucet handle.
    When the gripper is above the handle, grab it.
    - When the robot's gripper is vertically aligned with faucet handle and the robot's gripper is open, the robot should close gripper around faucet handle.
    Since we grabbed the handle and want to turn it, just rotate the gripper to the right.
    - When the robot's gripper is around faucet handle, the robot should rotate the gripper right.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Push the door closed
    First, put the gripper roughly above the door handle.
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    When the gripper is above the handle, put the gripper around the handle.
    - When the robot's gripper is above door handle and the robot's gripper is open, the robot should drop gripper around door handle.
    Once we grabbed the door handle, we can just push the door closed.
    - When the robot's gripper is around door handle, the robot should push door closed.

The task `peg-insert-vertical`