
    - 

The task `pick-hold` requires the robot to pick up the puck and hold it.
To pick up the puck and hold it reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the puck and the robot's gripper is above the puck, the robot should push the gripper to puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck, the robot should grab the puck.
    - When the robot's gripper is near the puck and the puck is above the robot's gripper, the robot should hold the puck.

The task `pick` requires the robot to pick up the puck.
To pick up the puck reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the puck, the robot should put gripper above puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should pick up the puck.

The task `stack` requires the robot to stack the pucks.
To stack the pucks reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the bottom puck, the robot should put the gripper above the bottom puck.
    - When the robot's gripper is vertically aligned with the bottom puck and the robot's gripper is not near the puck, the robot should push the gripper into the bottom puck.
    - When the robot's gripper is near the puck and the bottom puck is below the robot's gripper, the robot should pick up the puck.
    - When the puck is above the robot's gripper and the robot's gripper is vertically aligned with the puck on the top, the robot should push the puck into the top puck.
    - When the puck is near the top puck and the robot's gripper is not vertically aligned with the top puck, the robot should put gripper above top puck.
    - When the robot's gripper is vertically aligned with the top puck and the robot's gripper is not near the puck, the robot should push the gripper into the top puck.
    - When the robot's gripper is near the top puck and the top puck is below the robot's gripper, the robot should drop the puck.

The task `dis-stack` requires the robot to disassemble the stack of pucks