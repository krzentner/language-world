
    -
    -
    -
    -
    -
    -
    -
    -
    -
    -

The task `block-stack` requires the robot to pick up the block and place it on the table.
To pick up the block and place it on the table reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with block, the robot should put gripper above block.
    - When the robot's gripper is not around block and the robot's gripper is open, the robot should grab block.
    - When the robot's gripper is above block, the robot should lift block to table.
    - When the robot's gripper is above table, the robot should open gripper above table.

The task `lever-pull` requires the robot to pull the lever down.
To pull the lever down reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the lever, the robot should put gripper above lever.
    - When the robot's gripper is above the lever and the robot's gripper is not near the lever, the robot should push gripper into lever.
    - When the robot's gripper is near the lever and the lever is not pulled down, the robot should pull the lever down.

The task `sweep` requires the robot to push the puck to the target location.
To push the puck to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is near the puck, the robot should push puck to goal.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the door handle, the robot should put gripper above door handle.
    - When the robot's gripper is above door handle and the robot's gripper is not near door handle, the robot should push gripper into door handle.
    - When the robot's gripper is near the door handle, the robot should push door closed.

The task `faucet-close` requires the robot to turn the faucet right.
To turn the faucet right reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with faucet, the robot should put gripper above faucet.
    - When the robot's gripper is