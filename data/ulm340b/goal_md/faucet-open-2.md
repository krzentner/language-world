
    Steps:  1. Put gripper above the faucet  2. Grab the faucet  3. Turn it left  4. Turn it more left
    First, put the gripper above the faucet.
    - When the robot's gripper is not above the faucet, move the robot's gripper until the robot's gripper is vertically aligned with the faucet
    If the gripper isn't around the faucet, put it around the faucet.
    - When the robot's gripper is not around the faucet, move the robot's gripper until the robot's gripper is around the faucet and the robot's gripper is closed
    Now that the faucet is grabbed, we can turn it all the way left.
    - When the robot's gripper is around the faucet, move the robot's gripper until the robot's gripper is not left of the faucet

The task `sweep-right` requires the robot to push the puck right to the target location.
To push the puck right to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper above the puck  2. Push the puck to the right
    First, the gripper needs to be above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is above the puck
    Once the gripper is above the puck, push it to the right.
    - When the robot's gripper is above puck and the robot's gripper is not near puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck

The task `microwave-close` requires the robot to slide the microwave closed.
To slide the microwave closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper left of the microwave handle  2. Start pushing against the microwave handle to close the microwave  3. Push the microwave closed harder
    If the the microwave handle is right of the robot's gripper, we should move the gripper near the microwave handle to start pushing
    - When the robot's gripper is in front of the microwave handle, move the robot's gripper until the robot's gripper is left of the microwave handle
    If the robot's gripper is near the microwave handle we can probably slide the microwave closed now by moving the gripper left.
    - When the microwave handle is right of the robot's gripper and the robot's gripper is not near